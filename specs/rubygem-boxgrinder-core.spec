%define ruby_version 1.8
%define ruby_sitelib /usr/lib/ruby/site_ruby/%{ruby_version}
%define gemdir /usr/lib/ruby/gems/%{ruby_version}
%define gemname boxgrinder-core
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: BoxGrinder Core files
Name: rubygem-%{gemname}
Version: 0.0.3
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://www.jboss.org/stormgrind/projects/boxgrinder.html
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
BoxGrinder Core files


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
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Wed Mar 17 2010 Marek <goldmann@mistress.local> - 0.0.1-1
- Initial package
