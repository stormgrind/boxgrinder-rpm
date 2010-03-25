# Generated from amazon-ec2-0.9.7.gem by gem2rpm -*- rpm-spec -*-
%define ruby_version 1.8
%define ruby_sitelib /usr/lib/ruby/site_ruby/%{ruby_version}
%define gemdir /usr/lib/ruby/gems/%{ruby_version}
%define gemname amazon-ec2
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Amazon EC2 Ruby Gem
Name: rubygem-%{gemname}
Version: 0.9.9
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/grempe/amazon-ec2
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
Requires: rubygem(xml-simple) >= 1.0.12
#Requires: rubygem(mocha) >= 0.9.8
#Requires: rubygem(test-spec) >= 0.10.0
#Requires: rubygem(rcov) >= 0.9.6
#Requires: rubygem(perftools.rb) >= 0.3.9
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
A Ruby library for accessing the Amazon Web Services EC2, ELB, RDS,
Cloudwatch, and Autoscaling APIs.


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
%{_bindir}/ec2-gem-example.rb
%{_bindir}/ec2-gem-profile.rb
%{_bindir}/ec2sh
%{_bindir}/setup.rb
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/ChangeLog
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/README_dev.rdoc
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Wed Mar 25 2010 Marek <marek.goldmann@gmail.com> - 0.9.9-1
- Upgrade to upstream 0.9.9

* Wed Mar 17 2010 Marek <marek.goldmann@gmail.com> - 0.9.7-1
- Initial package

