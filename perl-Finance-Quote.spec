%define module	Finance-Quote
%define name	perl-%{module}
%define version 1.16
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Get stock and mutual fund quotes from various exchanges 
License:	GPL or Artistic
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Finance/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Requires:	perl-libwww-perl
Requires:	perl-HTML-TableExtract
Requires:	perl-CGI
Requires:	perl-HTML-Tree
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Finance::Quote provides access to time-delayed stockquotes from a
number of sources.  After you've installed the pacakage, try
'perldoc Finance::Quote' for full information.  Alternatively,
you can 'perldoc lib/Finance/Quote.pm' before the install.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc INSTALL ChangeLog Documentation/*
%{perl_vendorlib}/Finance
%{_mandir}/*/*


