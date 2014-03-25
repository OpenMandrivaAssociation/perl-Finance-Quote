%define modname	Finance-Quote
%define modver 1.28

Summary:	Get stock and mutual fund quotes from various exchanges 
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Finance/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires: perl(Time::Piece)
BuildRequires: perl(Mozilla::CA)
BuildRequires: perl(JSON)
BuildRequires: perl(Date::Calc)
BuildRequires: perl(Crypt::SSLeay)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(HTML::TableExtract)
BuildRequires:	perl(CGI)
BuildRequires:	perl(HTML::Tree)

%description
Finance::Quote provides access to time-delayed stockquotes from a
number of sources.  After you've installed the pacakage, try
'perldoc Finance::Quote' for full information.  Alternatively,
you can 'perldoc lib/Finance/Quote.pm' before the install.

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc   Documentation/*
%{perl_vendorlib}/Finance
%{_mandir}/man3/*




