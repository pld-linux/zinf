#
# Conditional build:
%bcond_without  alsa	# without alsa sound support
%bcond_without  arts	# without arts sound support
#
Summary:	MP3 audio player with theme user interface and streaming support
Summary(pl):	Odtwarzacz plików MP3 z obs³ug± motywów i streamingu
Name:		zinf
Version:	2.2.5
Release:	3
License:	GPL
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/zinf/%{name}-%{version}.tar.gz
# Source0-md5:	727db1d0d2673f68639d343ca0ec9895
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-ac.patch
Patch1:		%{name}-boost.patch
Patch2:		%{name}-musicbrainz.patch
URL:		http://www.zinf.org/
BuildRequires:	ORBit-devel >= 0.5.0
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 0.9.0}
%{?with_arts:BuildRequires:	artsc-devel}
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	boost-devel >= 1.31.0
BuildRequires:	boost-filesystem-devel >= 1.31.0
BuildRequires:	esound-devel >= 0.2.12
BuildRequires:	gdbm-devel
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	gettext-devel >= 0.13.1
BuildRequires:	id3lib-devel
BuildRequires:	libmusicbrainz-devel >= 2.0.1
BuildRequires:	libogg-devel >= 2:1.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	metakit-devel
%ifarch %{ix86}
BuildRequires:	nasm
%endif
BuildRequires:	ncurses-devel
BuildRequires:	xosd-devel
BuildRequires:	zlib-devel
Provides:	freeamp
Obsoletes:	freeamp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zinf is an extensible, cross-platform audio player. It features an
optimized version of the GPLed Xing MPEG decoder which makes it one of
the fastest and best sounding players available. Zinf provides a
number of the most common features users have come to expect in a
clean, easy to use interface.

This project was formely known as FreeAmp.

%description -l pl
Zinf jest rozszerzalnym, wieloplatformowym odtwarzaczem audio. Jego
zalety to zoptymalizowana wersja dekodera Xing MPEG (GPL) dziêki czemu
freeamp jest jednym z najszybszych i najlepszych odtwarzaczy. Zinf
daje funkcje, których zwykle u¿ytkownicy oczekuj± od prostego w
u¿ytkowaniu i jasnego interfejsu.

Ten program wcze¶niej by³ znany pod nazw± FreeAmp.

%package lmc-vorbis
Summary:	Ogg/Vorbis sound Logical Media Converter plugin for ZINF
Summary(pl):	Wtyczka konwertera mediów ZINF obs³uguj±ca d¼wiêk Ogg/Vorbis
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description lmc-vorbis
Ogg/Vorbis sound Logical Media Converter plugin for ZINF. This package
contains also Ogg/Vorbis MetaData Format plugin.

%description lmc-vorbis
Wtyczka konwertera mediów (Logical Media Converter) ZINF obs³uguj±ca
d¼wiêk Ogg/Vorbis. Pakiet zawiera dodatkowo wtyczkê formatu metadanych
(MetaData Format) ZINF obs³uguj±c± metadane z plików Ogg/Vorbis.

%package mdf-mbcd
Summary:	MusicBrainz MetaData Format plugin for ZINF
Summary(pl):	Wtyczka formatu metadanych ZINF obs³uguj±ca metadane MusicBrainz
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description mdf-mbcd
MusicBrainz MetaData Format plugin for ZINF.

%description mdf-mbcd -l pl
Wtyczka formatu metadanych (MetaData Format) ZINF obs³uguj±ca
metadane MusicBrainz.

%package pmo-alsa
Summary:	ALSA sound Physical Media Output plugin for ZINF
Summary(pl):	Wtyczka wyj¶cia mediów ZINF obs³uguj±ca wyj¶cie d¼wiêku ALSA
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description pmo-alsa
ALSA sound Physical Media Output plugin for ZINF.

%description pmo-alsa -l pl
Wtyczka wyj¶cia mediów (Physical Media Output) ZINF obs³uguj±ca
wyj¶cie d¼wiêku ALSA.

%package pmo-arts
Summary:	aRts sound Physical Media Output plugin for ZINF
Summary(pl):	Wtyczka wyj¶cia mediów ZINF obs³uguj±ca wyj¶cie d¼wiêku aRts
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description pmo-arts
aRts sound Physical Media Output plugin for ZINF.

%description pmo-arts -l pl
Wtyczka wyj¶cia mediów (Physical Media Output) ZINF obs³uguj±ca
wyj¶cie d¼wiêku aRts.

%package pmo-esound
Summary:	EsounD sound Physical Media Output plugin for ZINF
Summary(pl):	Wtyczka wyj¶cia mediów ZINF obs³uguj±ca wyj¶cie d¼wiêku EsounD
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description pmo-esound
ALSA sound Physical Media Output plugin for ZINF.

%description pmo-esound -l pl
Wtyczka wyj¶cia mediów (Physical Media Output) ZINF obs³uguj±ca
wyj¶cie d¼wiêku EsounD.

%package ui-corba
Summary:	CORBA User Interface plugin for ZINF
Summary(pl):	Wtyczka interfejsu ZINF obs³uguj±ca interfejs CORBA
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description ui-corba
CORBA User Interface plugin for ZINF.

%description ui-corba -l pl
Wtyczka interfejsu u¿ytkownika (User Interface) ZINF obs³uguj±ca
interfejs CORBA.

%package ui-gtk
Summary:	GTK+-based User Interface plugins for ZINF
Summary(pl):	Wtyczki interfejsu ZINF oparte na GTK+
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description ui-gtk
GTK+-based User Interface plugins for ZINF (albumart, download,
musicbrowser and zinf). It also contains Kjofol and Winamp Theme
Format plugins.

%description ui-gtk -l pl
Wtyczki interfejsu u¿ytkownika (User Interface) ZINF oparte na GTK+
(albumart, download, musicbrowser oraz zinf). Zawiera tak¿e wtyczki
formatu motywów (Theme Format) konwertuj±ce motywy Kjofola i Winampa.

%package ui-xosd
Summary:	XOSD User Interface plugin for ZINF
Summary(pl):	Wtyczka interfejsu ZINF oparta na XOSD
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description ui-xosd
XOSD User Interface plugin for ZINF.

%description ui-xosd -l pl
Wtyczka interfejsu u¿ytkownika (User Interface) ZINF oparta na XOSD.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
CPPFLAGS="-I/usr/include/ncurses"
%configure \
	%{!?with_alsa:--disable-alsa} \
	%{!?with_arts:--disable-arts} \
	--enable-corba \
	--enable-esd \
	--enable-rio \
%ifnarch %{ix86}
	--disable-x86opts \
%endif
	--enable-xosd

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README doc/{README.lcdui,README.linux,ThemeHowTo.txt,WISHLIST,user.txt}
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/cd.lmc
%attr(755,root,root) %{_libdir}/%{name}/plugins/wav.lmc
%attr(755,root,root) %{_libdir}/%{name}/plugins/xingmp3.lmc
%attr(755,root,root) %{_libdir}/%{name}/plugins/id3lib.mdf
%attr(755,root,root) %{_libdir}/%{name}/plugins/misc.mdf
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.plf
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.pmi
%attr(755,root,root) %{_libdir}/%{name}/plugins/cd.pmo
%attr(755,root,root) %{_libdir}/%{name}/plugins/soundcard.pmo
%attr(755,root,root) %{_libdir}/%{name}/plugins/wavout.pmo
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.ppp
%attr(755,root,root) %{_libdir}/%{name}/plugins/cmdline.ui
%attr(755,root,root) %{_libdir}/%{name}/plugins/irman.ui
%attr(755,root,root) %{_libdir}/%{name}/plugins/lcd.ui
%attr(755,root,root) %{_libdir}/%{name}/plugins/mpg123.ui
%attr(755,root,root) %{_libdir}/%{name}/plugins/ncurses.ui
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop

%files lmc-vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/vorbis.lmc
%attr(755,root,root) %{_libdir}/%{name}/plugins/vorbis.mdf

%files mdf-mbcd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/mbcd.mdf

%if %{with alsa}
%files pmo-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/alsa.pmo
%endif

%if %{with arts}
%files pmo-arts
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/arts.pmo
%endif

%files pmo-esound
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/esound.pmo

%files ui-corba
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/corba.ui

%files ui-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/kjofol.ftf
%attr(755,root,root) %{_libdir}/%{name}/plugins/winamp.ftf
%attr(755,root,root) %{_libdir}/%{name}/plugins/albumart.ui
%attr(755,root,root) %{_libdir}/%{name}/plugins/download.ui
%attr(755,root,root) %{_libdir}/%{name}/plugins/musicbrowser.ui
%attr(755,root,root) %{_libdir}/%{name}/plugins/zinf.ui
# only (graphical) themes here
%{_datadir}/%{name}

%files ui-xosd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/xosd.ui
