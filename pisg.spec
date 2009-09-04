%define name pisg
%define version 0.72
%define release %mkrel 3

Summary: An IRC channel statics generator
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
License: GPL
Group: Networking/IRC
Url: http://pisg.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: perl
BuildArch: noarch

%description
pisg is an IRC channel statics generator written in Perl, it creates
statistics from different logfile formats. It was originally written
because IRCStats wasn't open source. So here's an open source/GPL'ed
version to anyone interested. It's a funny thing for your IRC channel,
and it's highly customizeable.

%prep
%setup -q

%build
# Some default configuration setting
perl -pi -e "s:configfile => 'pisg.cfg':configfile => '%_sysconfdir/pisg.cfg':" modules/Pisg.pm
perl -pi -e "s:langfile => 'lang.txt':langfile => '%_datadir/%name/lang.txt':" modules/Pisg.pm
perl -pi -e "s:cssdir => 'layout/':cssdir => '%_datadir/%name/layout/':" modules/Pisg.pm

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p %buildroot%_bindir
mkdir -p %buildroot%perl_vendorlib
mkdir -p %buildroot%{_datadir}/%{name}
mkdir -p %buildroot%_sysconfdir

install -m 755 pisg %buildroot%_bindir
cp -ar modules/* %buildroot%perl_vendorlib
cp -ar lang.txt layout %buildroot%{_datadir}/%{name}
cp -a pisg.cfg %buildroot%_sysconfdir

find %buildroot%perl_vendorlib -type f -exec chmod 644 {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README docs
%doc scripts gfx
%_bindir/%{name}
%perl_vendorlib/*
%_datadir/%name
%config(noreplace) %_sysconfdir/pisg.cfg



