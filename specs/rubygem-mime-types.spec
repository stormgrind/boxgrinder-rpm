%define ruby_version 1.8
%define ruby_sitelib /usr/lib/ruby/site_ruby/%{ruby_version}
%define gemdir /usr/lib/ruby/gems/%{ruby_version}
%define gemname mime-types
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Manages a MIME Content-Type database that will return the Content-Type for a given filename
Name: rubygem-%{gemname}
Version: 1.16
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://mime-types.rubyforge.org/
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
Requires: rubygem(archive-tar-minitar) >= 0.5
Requires: rubygem(nokogiri) >= 1.2
Requires: rubygem(rcov) >= 0.8
Requires: rubygem(hoe) >= 1.8.3
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
MIME::Types for Ruby originally based on and synchronized with MIME::Types for
Perl by Mark Overmeer, copyright 2001 - 2009. As of version 1.15, the data
format for the MIME::Type list has changed and the synchronization will no
longer happen.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/History.txt
%doc %{geminstdir}/Install.txt
%doc %{geminstdir}/Licence.txt
%doc %{geminstdir}/README.txt
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Wed Mar 17 2010 Marek <goldmann@mistress.local> - 1.16-1
- Initial package
