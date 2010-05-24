%define tb_version 1.0.0.Beta19
%define reflog c950e07

Summary:        BoxGrinder REST is a REST service for BoxGrinder
Name:           boxgrinder-rest
Version:        0.0.1
Release:        1
License:        LGPL
BuildArch:      noarch
Group:          Development/Tools
URL:            http://www.jboss.org/stormgrind/projects/boxgrinder/rest.html
Source0:        http://github.com/stormgrind/%{name}/tarball/%{version}
Source1:        http://repository.torquebox.org/maven2/releases/org/torquebox/torquebox-bin/%{tb_version}/torquebox-bin-%{tb_version}.zip
Source2:        %{name}.init
Requires:           java-1.6.0-openjdk
Requires:           postgresql-server
Requires:           shadow-utils
Requires(build):    unzip
Requires:           coreutils
Requires:           initscripts
Requires(post):     /sbin/chkconfig
BuildRoot:          %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%define runuser %{name}
%define __jar_repack %{nil}

%description
BoxGrinder REST is a REST service for BoxGrinder

%prep
%setup -b 0 -n stormgrind-%{name}-%{reflog}

cd %{_topdir}/BUILD

rm -rf torquebox-%{tb_version}-bin
unzip -q %{SOURCE1}

%install
rm -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT/opt/%{name}-%{version}/%{name}
install -d -m 755 $RPM_BUILD_ROOT/opt/%{name}-%{version}/torquebox

cd %{_topdir}/BUILD

rm -rf torquebox-%{tb_version}-bin/jboss/server/all
rm -rf torquebox-%{tb_version}-bin/jboss/server/minimal
rm -rf torquebox-%{tb_version}-bin/jboss/server/standard
rm -rf torquebox-%{tb_version}-bin/jboss/server/jbossweb-standalone

# it caused adding bad requires for package
rm -rf torquebox-%{tb_version}-bin/jboss/bin/jboss_init_solaris.sh

cp -R stormgrind-%{name}-%{reflog}/* $RPM_BUILD_ROOT/opt/%{name}-%{version}/%{name}
cp -R torquebox-%{tb_version}-bin/* $RPM_BUILD_ROOT/opt/%{name}-%{version}/torquebox

chmod 755 $RPM_BUILD_ROOT/opt/%{name}-%{version}/torquebox/jruby

$RPM_BUILD_ROOT/opt/%{name}-%{version}/torquebox/jruby/bin/jruby -S gem install boxgrinder-core

install -d -m 755 $RPM_BUILD_ROOT/etc/sysconfig

echo "BG_REST_HOME=/opt/%{name}-%{version}/%{name}"  > $RPM_BUILD_ROOT/etc/sysconfig/%{name}
echo "BG_REST_VERSION=%{version}"                   >> $RPM_BUILD_ROOT/etc/sysconfig/%{name}

cat > $RPM_BUILD_ROOT/opt/%{name}-%{version}/torquebox/jboss/server/default/deploy/%{name}-rails.yml <<EOF
---
application:
  RAILS_ROOT: /opt/%{name}-%{version}/%{name}
  RAILS_ENV: production
web:
  context: /
EOF

install -d -m 755 $RPM_BUILD_ROOT%{_initrddir}
install -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_initrddir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add %{name}

%pre
/usr/sbin/groupadd -r %{name} 2>/dev/null || :
/usr/sbin/useradd -c "BoxGrinder REST" -r -s /bin/bash -d /opt/%{name}-%{version} -g %{name} %{name} 2>/dev/null || :

%files
%defattr(-,%{name},%{name})
/

%changelog
* Fri May 21 2010 Marek Goldmann <marek.goldmann@gmail.com> - 0.1.0-1
- Initial package
