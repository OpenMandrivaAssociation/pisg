%define name pisg
%define version 0.72
%define release %mkrel 4

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





%changelog
* Tue May 03 2011 Michael Scherer <misc@mandriva.org> 0.72-4mdv2011.0
+ Revision: 664798
- rebuild old package

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.72-3mdv2010.0
+ Revision: 430737
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.72-2mdv2009.0
+ Revision: 269000
- rebuild early 2009.0 package (before pixel changes)

* Tue Jun 03 2008 Olivier Thauvin <nanardon@mandriva.org> 0.72-1mdv2009.0
+ Revision: 214654
- 0.72

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.71-1mdv2008.1
+ Revision: 140731
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Mar 03 2007 Olivier Thauvin <nanardon@mandriva.org> 0.71-1mdv2007.0
+ Revision: 131718
- 0.71

* Sat Dec 09 2006 Olivier Thauvin <nanardon@mandriva.org> 0.70-1mdv2007.1
+ Revision: 93975
- 0.70

* Tue Aug 08 2006 Olivier Thauvin <nanardon@mandriva.org> 0.68-2mdv2007.0
+ Revision: 54199
- rebuild
- Import pisg

* Wed Apr 19 2006 Olivier Thauvin <nanardon@mandriva.org> 0.68-1mdk
- 0.68

* Tue Sep 06 2005 Olivier Thauvin <nanardon@mandriva.org> 0.67-1mdk
- 0.67

* Sat Jun 25 2005 Erwan Velu <erwan@seanodes.com> 0.66-1mdk
- 0.66

* Fri May 06 2005 Olivier Thauvin <nanardon@mandriva.org> 0.65-1mdk
- 0.65

* Fri Apr 15 2005 Erwan Velu <erwan@seanodes.com> 0.64-1mdk
- 0.64

* Mon Dec 13 2004 Olivier Thauvin <nanardon@mandrake.org> 0.62-1mdk
- First mdk package

