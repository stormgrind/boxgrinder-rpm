%define ruby_version 1.8
%define ruby_sitelib /usr/lib/ruby/site_ruby/%{ruby_version}
%define gemdir /usr/lib/ruby/gems/%{ruby_version}
%define gemname xml-simple
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: A simple API for XML processing
Name: rubygem-%{gemname}
Version: 1.0.12
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://xml-simple.rubyforge.org
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
A simple API for XML processing.


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
* Wed Mar 17 2010 Marek <goldmann@mistress.local> - 1.0.12-1
- Initial package

