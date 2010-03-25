%define ruby_version 1.8
%define ruby_sitelib /usr/lib/ruby/site_ruby/%{ruby_version}
%define gemdir /usr/lib/ruby/gems/%{ruby_version}
%define gemname builder
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Builders for MarkUp
Name: rubygem-%{gemname}
Version: 2.1.2
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://onestepback.org
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Builder provides a number of builder objects that make creating structured
data simple to do.  Currently the following builder objects are supported:  *
XML Markup * XML Events


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
%doc %{geminstdir}/CHANGES
%doc %{geminstdir}/Rakefile
%doc %{geminstdir}/README
%doc %{geminstdir}/doc/releases/builder-1.2.4.rdoc
%doc %{geminstdir}/doc/releases/builder-2.0.0.rdoc
%doc %{geminstdir}/doc/releases/builder-2.1.1.rdoc
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Wed Mar 17 2010 Marek <goldmann@mistress.local> - 2.1.2-1
- Initial package
