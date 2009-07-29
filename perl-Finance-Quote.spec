%define upstream_name	 Finance-Quote
%define upstream_version 1.16

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Get stock and mutual fund quotes from various exchanges 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Finance/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:       perl-libwww-perl
BuildRequires:       perl-HTML-TableExtract
BuildRequires:       perl-CGI
BuildRequires:       perl-HTML-Tree
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
Requires:	perl-libwww-perl
Requires:	perl-HTML-TableExtract
Requires:	perl-CGI
Requires:	perl-HTML-Tree

%description
Finance::Quote provides access to time-delayed stockquotes from a
number of sources.  After you've installed the pacakage, try
'perldoc Finance::Quote' for full information.  Alternatively,
you can 'perldoc lib/Finance/Quote.pm' before the install.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
