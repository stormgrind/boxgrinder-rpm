%define ruby_version 1.8
%define ruby_sitelib /usr/lib/ruby/site_ruby/%{ruby_version}
%define gemdir /usr/lib/ruby/gems/%{ruby_version}
%define gemname boxgrinder-build
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: BoxGrinder Build files
Name: rubygem-%{gemname}
Version: 0.2.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://www.jboss.org/stormgrind/projects/boxgrinder.html
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
Requires: rubygem(boxgrinder-core) >= 0.0.4
Requires: rubygem(aws-s3) >= 0.6.2
Requires: rubygem(amazon-ec2) >= 0.9.6
Requires: rubygem(net-sftp) >= 2.0.4
Requires: rubygem(net-ssh) >= 2.0.20
Requires: rubygem(rake) >= 0.8.7
Requires: gcc, gcc-c++, make, rubygem-rake, wget, rpmdevtools, java-1.6.0-openjdk-devel, autoconf, expect, appliance-tools, sudo, libguestfs, ruby-libguestfs, guestfish, zlib-devel, SDL-devel, boxgrinder-environment, yum-utils, qemu-stable
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
BoxGrinder Build files

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
%{_bindir}/boxgrinder
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%changelog
* Wed Mar 17 2010 Marek Goldmann <marek.goldmann@gmail.com> - 0.0.1-1
- Initial package
