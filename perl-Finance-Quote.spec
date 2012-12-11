%define upstream_name	 Finance-Quote
%define upstream_version 1.17

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Get stock and mutual fund quotes from various exchanges 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Finance/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(HTML::TableExtract)
BuildRequires:	perl(CGI)
BuildRequires:	perl(HTML::Tree)
BuildArch:	noarch

%description
Finance::Quote provides access to time-delayed stockquotes from a
number of sources.  After you've installed the pacakage, try
'perldoc Finance::Quote' for full information.  Alternatively,
you can 'perldoc lib/Finance/Quote.pm' before the install.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc INSTALL ChangeLog Documentation/*
%{perl_vendorlib}/Finance
%{_mandir}/*/*


%changelog
* Tue Oct 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.170.0-1mdv2010.0
+ Revision: 454468
- new version
- no need for explicit dependencies

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.160.0-1mdv2010.0
+ Revision: 403183
- rebuild using %%perl_convert_version

* Sun May 10 2009 Frederik Himpe <fhimpe@mandriva.org> 1.16-1mdv2010.0
+ Revision: 374101
- Add perl- packages as BuildRequires too
- Change BuildRequires in Requires for perl- packages: these are also
  required at run-time
- add Perl-HTML-Tree and perl-CGI Requires
- Add perl-HTML-TableExtract BuildRequires for test suite
- Add perl-libwww-perl BuildRequires to make the test suite succeed
- update to new version 1.16

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.13-3mdv2009.0
+ Revision: 257040
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.13-1mdv2008.1
+ Revision: 135841
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.13-1mdv2008.0
+ Revision: 46527
- update to new version 1.13


* Thu Nov 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.12-1mdv2007.0
+ Revision: 84626
- new version
- Import perl-Finance-Quote

* Fri Sep 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-2mdv2007.0
- Rebuild

* Wed Mar 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-1mdk
- New release 1.11
- spec cleanup

* Thu Jul 21 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.10-1mdk
- 1.10 ; add tests

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.08-3mdk
- fix buildrequires in a backward compatible way

* Sat Jul 24 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.08-2mdk 
- rpmbuildupdate aware

