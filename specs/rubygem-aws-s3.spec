# Generated from aws-s3-0.6.2.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname aws-s3
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Client library for Amazon's Simple Storage Service's REST API
Name: rubygem-%{gemname}
Version: 0.6.2
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://amazon.rubyforge.org
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
Requires: rubygem(xml-simple) >= 0
Requires: rubygem(builder) >= 0
Requires: rubygem(mime-types) >= 0
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Client library for Amazon's Simple Storage Service's REST API


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/s3sh
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README
%doc %{geminstdir}/COPYING
%doc %{geminstdir}/INSTALL
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Wed Mar 17 2010 Marek <goldmann@mistress.local> - 0.6.2-1
- Initial package

