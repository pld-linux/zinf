Summary:	MP3 audio player with theme user interface and streaming support
Summary(pl):	Odtwarzacz plik�w MP3 z obs�ug� temat�w i streamingu
Name:		zinf
Version:	2.2.0
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/zinf/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-ncurses_include.patch
Patch1:		%{name}-make.patch
Patch2:		%{name}-ac.patch
Patch3:		%{name}-DESTDIR.patch
URL:		http://www.zinf.org/
BuildRequires:	ORBit-devel
BuildRequires:	arts-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel >= 0.2.12
BuildRequires:	freetype1-devel
BuildRequires:	gdk-pixbuf-devel >= 0.8.0
BuildRequires:	gtk+-devel >= 1.2.5
BuildRequires:	id3lib-devel
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	musicbrainz-devel >= 1.1.0
BuildRequires:	ncurses-devel
%ifarch %{ix86}
BuildRequires:	nasm
%endif
BuildRequires:	zlib-devel
Provides:	freeamp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	freeamp

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Zinf is an extensible, cross-platform audio player. It features an
optimized version of the GPLed Xing MPEG decoder which makes it one of
the fastest and best sounding players available. Zinf provides a
number of the most common features users have come to expect in a
clean, easy to use interface.

This project was formely known as FreeAmp.

%description -l pl
Zinf jest rozszerzalnym, wieloplatformowym odtwarzaczem audio. Jego
zalety to zoptymalizowana wersja dekodera Xing MPEG (GPL) dzi�ki czemu
freeamp jest jednym z najszybszych i najlepszych odtwarzaczy. Zinf
daje funkcje, kt�rych zwykle u�ytkownicy oczekuj� od prostego w
u�ytkowaniu i jasnego interfejsu.

Ten program wczesniej by� znany pod nazw� FreeAmp.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
cp -f /usr/share/automake/config.* config/
%{__aclocal}
autoconf
%configure \
	--disable-alsa \
	--enable-arts \
	--enable-esd \
	--enable-cmdline \
%ifnarch %{ix86}
	--disable-x86opts \
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Multimedia

%{__make} \
	DESTDIR=$RPM_BUILD_ROOT \
	install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES NEWS README README.linux
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.dlf
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.ftf
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.lmc
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.mdf
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.plf
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.pmi
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.pmo
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.ui
%{_pixmapsdir}/*
%{_applnkdir}/Multimedia/*
%{_libdir}/%{name}/plugins/*.xml
%{_datadir}/%{name}
