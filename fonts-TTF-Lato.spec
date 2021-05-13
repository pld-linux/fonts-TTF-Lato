Summary:	Lato font family
Name:		fonts-TTF-Lato
Version:	2.015
Release:	1
License:	OFL
Group:		Fonts
Source0:	https://www.latofonts.com/download/Lato2OFL.zip
# Source0-md5:	29e379a6ecc1b86c96931fa6ce4b3b0c
URL:		https://www.latofonts.com/
Suggests:	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
Lato is a sanserif typeface family designed in the Summer 2010 and
extended in the Summer 2013 by Warsaw-based designer Lukasz Dziedzic
("Lato" means "Summer" in Polish). It tries to carefully balance some
potentially conflicting priorities: it should seem quite "transparent"
when used in body text but would display some original traits when
used in larger sizes. The classical proportions, particularly visible
in the uppercase, give the letterforms familiar harmony and elegance.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ttffontsdir}

cp -p Lato2OFL/*.ttf $RPM_BUILD_ROOT%{_ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- fontpostinst
if [ "$1" = "1" ] && [ "$2" = "1" ]; then
	fontpostinst TTF
fi

%triggerun -- fontpostinst
if [ "$1" = "0" ] || [ "$2" = "0" ]; then
	fontpostinst TTF
fi

%files
%defattr(644,root,root,755)
%doc Lato2OFL/README.txt
%{_ttffontsdir}/Lato-*.ttf
