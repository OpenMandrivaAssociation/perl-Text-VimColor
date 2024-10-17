%define upstream_name    Text-VimColor
%define upstream_version 0.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Syntax color text in HTML or XML using Vim
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Path::Class)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module tries to markup text files according to their syntax. It can be
used to produce web pages with pretty-printed colourful source code
samples. It can produce output in the following formats:

* HTML

  Valid XHTML 1.0, with the exact colouring and style left to a CSS
  stylesheet

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
# If the terminal is not set, then the tests will fail, so skip them.
if test -z "$TERM" ; then 
    true
else 
    %{make} test
fi

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc ChangeLog README
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/text-vimcolor
/usr/share/man/man1/text-vimcolor.1.lzma

