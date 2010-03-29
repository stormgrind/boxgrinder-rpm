%define maven_version 2.2.1

Summary:        BoxGrinder environment
Name:           boxgrinder-environment
Version:        1.0.0.Beta2
Release:        1
License:        LGPL
BuildArch:      noarch
Group:          Applications/System
Source0:        http://www.apache.org/dist/maven/binaries/apache-maven-2.2.1-bin.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires(pre):  shadow-utils, coreutils, sudo

%description
BoxGrinder environment. Required tools and source code for building appliances.

%prep
%setup -n apache-maven-%{maven_version}

%install
rm -Rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT/opt/%{name}/tools/apache-maven-%{maven_version}

cp -R * $RPM_BUILD_ROOT/opt/%{name}/tools/apache-maven-%{maven_version}

%clean
rm -Rf $RPM_BUILD_ROOT

%post
/usr/sbin/useradd -m -p '$1$LxTRJ/$WIyjiQ5521QRECVt9Ded90' boxgrinder
/bin/chown boxgrinder:boxgrinder /opt/%{name} -R

/bin/echo "mkdir /mnt/boxgrinder" >> /etc/rc.local
/bin/echo "chown boxgrinder:boxgrinder /mnt/boxgrinder" >> /etc/rc.local
/bin/echo "options loop max_loop=64" >> /etc/modprobe.d/loop.conf

/bin/echo "### BoxGrinder vars, do not modify these lines! ###" >> /home/boxgrinder/.bashrc
/bin/echo "export PATH=$PATH:/opt/%{name}/tools/apache-maven-%{maven_version}/bin:/usr/local/bin" >> /home/boxgrinder/.bashrc
/bin/echo "export JAVA_HOME=/usr/lib/jvm/java-openjdk" >> /home/boxgrinder/.bashrc
/bin/echo -e "boxgrinder    ALL=(ALL)       NOPASSWD: ALL\nDefaults:boxgrinder env_keep+=\"PYTHONUNBUFFERED\"" > /etc/sudoers.d/boxgrinder

chmod 0440 /etc/sudoers.d/boxgrinder

%preun
rm -rf /etc/sudoers.d/boxgrinder

%files
%defattr(-,root,root)
/

%changelog
* Wed May 13 2009 Marek Goldmann 1.0.0.Beta2-1
- Using sudoers.d/ directory
