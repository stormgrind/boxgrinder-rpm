# Generated from net-sftp-2.0.4.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname net-sftp
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: A pure Ruby implementation of the SFTP client protocol
Name: rubygem-%{gemname}
Version: 2.0.4
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://net-ssh.rubyforge.org/sftp
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
Requires: rubygem(net-ssh) >= 2.0.9
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
A pure Ruby implementation of the SFTP client protocol


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
%doc %{geminstdir}/CHANGELOG.rdoc
%doc %{geminstdir}/README.rdoc
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Wed Mar 17 2010 Marek <goldmann@mistress.local> - 2.0.4-1
- Initial package
