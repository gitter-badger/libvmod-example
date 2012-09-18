Summary: varnish-libvmod-example
Name: varnish-libvmod-example
Version: 0.1
Release: 1%{?dist}
License: BSD
Group: System Environment/Daemons
# for now, lets build i386 and x86_64 explicitly.
#BuildArch: noarch
#URL: http://github.com/varnish/varnish-agent/
#Source0: ./%{name}.tar.gz
Source0: ./libvmod-example.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: varnish > 3.0
BuildRequires: make, autoconf, automake, libtool, python-docutils
# you need EPEL
#Requires: perl-Log-Log4perl
#Requires: perl-Digest-SHA
#Requires(post): /sbin/chkconfig
#Requires(preun): /sbin/chkconfig
##Requires(preun): /sbin/service
#%if %{undefined suse_version}
#Requires(preun): initscripts
#%endif

%description
libvmod-example

%prep
%setup -n libvmod-example

%build
./autogen.sh
# this is a hack and assumes a prebuilt copy of varnish in VARNISHSRC.
./configure VARNISHSRC=$HOME/varnish-cache/ VMODDIR=/usr/lib64/varnish/vmods/ --prefix=/usr/
make

%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/usr/share/doc/%{name}/ 
cp README.rst %{buildroot}/usr/share/doc/%{name}/
cp COPYING %{buildroot}/usr/share/doc/%{name}/

#mkdir -p %{buildroot}/usr/sbin/ 
#mv %{buildroot}/usr/local/sbin/* %{buildroot}/usr/sbin/

#mkdir -p %{buildroot}/etc/init.d/
#mkdir -p %{buildroot}/etc/varnish/
#mkdir -p %{buildroot}/etc/sysconfig/
##mkdir -p %{buildroot}/etc/varnish-agent/
#mkdir -p %{buildroot}/var/lib/varnish-agent/
#mkdir -p %{buildroot}/usr/share/doc/varnish-agent/examples/

#cp src/varnish-agent      %{buildroot}/usr/bin/
#cp example-agent.conf     %{buildroot}/usr/share/doc/varnish-agent/examples/agent.conf
#cp example-agent.conf     %{buildroot}/etc/varnish/agent.conf
#
#cp LICENCE.txt %{buildroot}/usr/share/doc/varnish-agent/
#cp README.rst  %{buildroot}/usr/share/doc/varnish-agent/
##
#cp redhat/varnish-agent.initrc    %{buildroot}/etc/init.d/varnish-agent
#cp redhat/varnish-agent.sysconfig %{buildroot}/etc/sysconfig/varnish-agent

#mkdir -p %{buildroot}/%{_mandir}/man1/
#%{buildroot}/usr/bin/varnish-agent --man > %{buildroot}/%{_mandir}/man1/varnish-agent.1
#
#

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
#%{_sbindir}/vstatd
# /opt/varnish/lib/varnish/vmods/
/usr/lib64/varnish/vmods/
%doc /usr/share/doc/%{name}/*

#%{_libdir}/varnish
#%{_var}/lib/varnish-agent
#%{_var}/log/varnish
#%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*
#%{_mandir}/man7/*.7*
#%doc /usr/share/doc/varnish-agent/*

#%doc examples
#%dir %{_sysconfdir}/varnish/
#%config(noreplace) %{_sysconfdir}/varnish-agent.conf
#%config(noreplace) /etc/varnish/agent.conf
#%config(noreplace) /etc/sysconfig/varnish-agent

%preun
#if [ $1 -lt 1 ]; then
#/sbin/service varnish-agent stop > /dev/null 2>&1
#/sbin/chkconfig --del varnish-agent
#fi

%changelog
* Thu Sep 18 2012 Lasse Karstensen <lasse@varnish-software.com> - 0.1-0.20120918
- Initial version.
