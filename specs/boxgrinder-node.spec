%define jruby_version 1.5.0
%define reflog 81e8313

Summary:        BoxGrinder Node is a builder service for BoxGrinder REST
Name:           boxgrinder-node
Version:        0.0.2
Release:        1
License:        CPL/GPL/LGPL
BuildArch:      noarch
Group:          Development/Tools
URL:            http://www.jboss.org/stormgrind/projects/boxgrinder/rest.html
Source0:        http://github.com/stormgrind/%{name}/tarball/%{version}
Source1:        http://jruby.org.s3.amazonaws.com/downloads/%{jruby_version}/jruby-bin-%{jruby_version}.tar.gz
Source2:        %{name}.init
Source3:        http://repo.boxgrinder.org/boxgrinder/gems/torquebox-messaging-runtime-1.0.0.gem
Source4:        http://repo.boxgrinder.org/boxgrinder/gems/torquebox-messaging-client-1.0.0.gem
Source5:        http://repo.boxgrinder.org/boxgrinder/gems/torquebox-messaging-container-1.0.0.gem
Requires:       shadow-utils
Requires:       coreutils
Requires:       initscripts
Requires(post): /sbin/chkconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
BoxGrinder Node is a builder service for BoxGrinder REST

%prep
%setup -b 0 -n stormgrind-%{name}-%{reflog}
%setup -b 1 -n jruby-%{jruby_version}

%install
rm -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT/opt/%{name}-%{version}/%{name}
install -d -m 755 $RPM_BUILD_ROOT/opt/%{name}-%{version}/jruby

cd %{_topdir}/BUILD

rm stormgrind-%{name}-%{reflog}/%{name}.gemspec

cp -R stormgrind-%{name}-%{reflog}/* $RPM_BUILD_ROOT/opt/%{name}-%{version}/%{name}
cp -R jruby-%{jruby_version}/* $RPM_BUILD_ROOT/opt/%{name}-%{version}/jruby

$RPM_BUILD_ROOT/opt/%{name}-%{version}/jruby/bin/jruby -S gem install boxgrinder-core %{SOURCE3} %{SOURCE4} %{SOURCE5}

install -d -m 755 $RPM_BUILD_ROOT/etc/sysconfig

echo "BG_NODE_HOME=/opt/%{name}-%{version}/%{name}"  > $RPM_BUILD_ROOT/etc/sysconfig/%{name}
echo "JRUBY_HOME=/opt/%{name}-%{version}/jruby"     >> $RPM_BUILD_ROOT/etc/sysconfig/%{name}

chmod +x $RPM_BUILD_ROOT/opt/%{name}-%{version}/%{name}/bin/%{name} 

install -d -m 755 $RPM_BUILD_ROOT%{_initrddir}
install -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_initrddir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT/var/log/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add %{name}

%pre
/usr/sbin/groupadd -r %{name} 2>/dev/null || :
/usr/sbin/useradd -c "BoxGrinder Node" -r -s /bin/bash -d /opt/%{name}-%{version} -g %{name} %{name} 2>/dev/null || :

%files
%defattr(-,%{name},%{name})
/

%changelog
* Fri May 21 2010 Marek Goldmann <marek.goldmann@gmail.com> - 0.0.2-1
- Initial package
