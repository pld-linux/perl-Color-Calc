#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Color
%define		pnam	Calc
Summary:	Simple calculations with RGB colors
Summary(pl.UTF-8):	Proste obliczenia na kolorach RGB
Name:		perl-Color-Calc
Version:	1.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Color/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9a474f4600fb0381461fbd6b20ca0e1c
URL:		http://search.cpan.org/dist/Color-Calc/
BuildRequires:	perl-Graphics-ColorNames
BuildRequires:	perl-Graphics-ColorNames-WWW
BuildRequires:	perl-Graphics-ColorObject
BuildRequires:	perl-Params-Validate
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple calculations with RGB colors.

%description -l pl.UTF-8
Proste obliczenia na kolorach RGB.

%prep
%setup -q %{version}q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Color/*.pm
%dir %{perl_vendorlib}/Color/Calc
%{perl_vendorlib}/Color/Calc/*.pm
%{_mandir}/man3/*
