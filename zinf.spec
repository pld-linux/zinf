#
# Conditional build:
# _without_arts:	- without arts sound support
#
Summary:	MP3 audio player with theme user interface and streaming support
Summary(pl):	Odtwarzacz plików MP3 z obs³ug± motywów i streamingu
Name:		zinf
Version:	2.2.4
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/zinf/%{name}-%{version}.tar.gz
# Source0-md5:	7520bbbffa466b86753c461f3c3a075f
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-ncurses_include.patch
Patch1:		%{name}-ac.patch
#Patch2:		%{name}-DESTDIR.patch
URL:		http://www.zinf.org/
BuildRequires:	ORBit-devel
%{!?_without_arts:BuildRequires:	artsc-devel}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel >= 0.2.12
BuildRequires:	freetype1-devel
BuildRequires:	gdk-pixbuf-devel >= 0.8.0
BuildRequires:	gtk+-devel >= 1.2.5
BuildRequires:	id3lib-devel
BuildRequires:	libmusicbrainz-devel >= 1.1.0
BuildRequires:	libogg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
%ifarch %{ix86}
BuildRequires:	nasm
%endif
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
Provides:	freeamp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	freeamp

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

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-alsa \
	%{?_without_arts:--disable-arts} \
	--enable-esd \
	--enable-cmdline \
%ifnarch %{ix86}
	--disable-x86opts \
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Multimedia,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README doc/{README.lcdui,README.linux,ThemeHowTo.txt,WISHLIST,user.txt}
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.ftf
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.lmc
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.mdf
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.plf
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.pmi
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.pmo
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.ui
%{_pixmapsdir}/*
%{_applnkdir}/Multimedia/*
%{_datadir}/%{name}
