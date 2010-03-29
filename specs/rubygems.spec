%define gem_dir /usr/lib/ruby/gems
%define rb_ver 1.8
%define gem_home %{gem_dir}/%{rb_ver}
%define ruby_sitelib /usr/lib/ruby/site_ruby/%{rb_ver}

Summary: The Ruby standard for packaging ruby libraries
Name: rubygems
Version: 1.3.6
Release: 1%{?dist}
Group: Development/Libraries
# No GPL version is specified.
License: Ruby or GPL+
URL: http://rubyforge.org/projects/rubygems
Source0: http://rubyforge.org/frs/download.php/69365/rubygems-1.3.6.tgz
Patch0: rubygems-%{version}-noarch-gemdir.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
Requires: ruby(abi) = 1.8 ruby-rdoc
BuildRequires:  ruby ruby-rdoc
BuildArch: noarch
Provides: ruby(rubygems) = %{version}

%description
RubyGems is the Ruby standard for publishing and managing third party
libraries.

%prep
%setup -q
%patch0 -p1

# Some of the library files start with #! which rpmlint doesn't like
# and doesn't make much sense
for f in `find lib -name \*.rb` ; do
  head -1 $f | grep -q '^#!/usr/bin/env ruby' && sed -i -e '1d' $f
done

%build
# Nothing

%install
rm -rf $RPM_BUILD_ROOT
GEM_HOME=%{buildroot}/%{gem_home} \
    ruby setup.rb --prefix=%{_prefix} \
        --no-rdoc --no-ri \
        --destdir=%{buildroot}/%{ruby_sitelib}/

mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}/%{ruby_sitelib}/usr/bin/gem %{buildroot}/%{_bindir}/gem
rm -rf %{buildroot}/%{ruby_sitelib}/bin
mv %{buildroot}/%{ruby_sitelib}/usr/lib/* %{buildroot}/%{ruby_sitelib}/.

pwd

mkdir -p %{buildroot}/%{gem_home}/cache %{buildroot}/%{gem_home}/gems %{buildroot}/%{gem_home}/specifications %{buildroot}/%{gem_home}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%doc README ChangeLog
%doc GPL.txt LICENSE.txt Manifest.txt History.txt
%dir %{gem_dir}
%dir %{gem_home}
%dir %{gem_home}/cache
%dir %{gem_home}/gems
%dir %{gem_home}/specifications
%doc %{gem_home}/doc
%{_bindir}/gem
%{ruby_sitelib}/*

%changelog
* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 09 2008 Jeroen van Meeuwen <kanarip@kanarip.com> - 1.3.1-1
- New upstream version

* Tue Sep 16 2008 David Lutterkort <dlutter@redhat.com> - 1.2.0-2
- Bump release because I forgot to check in newer patch

* Tue Sep 16 2008 David Lutterkort <dlutter@redhat.com> - 1.2.0-1
- Updated for new setup.rb
- Simplified by removing conditionals that were needed for EL-4;
  there's just no way we can support that with newer rubygems

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.4-2
- fix license tag

* Fri Jul 27 2007 David Lutterkort <dlutter@redhat.com> - 0.9.4-1
- Conditionalize so it builds on RHEL4

* Tue Feb 27 2007 David Lutterkort <dlutter@redhat.com> - 0.9.2-1
- New version
- Add patch0 to fix multilib sensitivity of Gem::dir (bz 227400)

* Thu Jan 18 2007 David Lutterkort <dlutter@redhat.com> - 0.9.1-1
- New version; include LICENSE.txt and GPL.txt
- avoid '..' in gem_dir to work around a bug in gem installer
- add ruby-rdoc to requirements

* Tue Jan  2 2007 David Lutterkort <dlutter@redhat.com> - 0.9.0-2
- Fix gem_dir to be arch independent
- Mention dual licensing in License field

* Fri Dec 22 2006 David Lutterkort <dlutter@redhat.com> - 0.9.0-1
- Updated to 0.9.0
- Changed to agree with Fedora Extras guidelines

* Mon Jan  9 2006 David Lutterkort <dlutter@redhat.com> - 0.8.11-1
- Updated for 0.8.11

* Sun Oct 10 2004 Omar Kilani <omar@tinysofa.org> 0.8.1-1ts
- First version of the package
