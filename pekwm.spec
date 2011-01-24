Summary:	pekwm - based on the aewm++ window manager
Summary(pl.UTF-8):	pekwm - zarządca okien oparty na aewm++
Name:		pekwm
Version:	0.1.12
Release:	1
License:	GPL v2
Group:		X11/Window Managers
Source0:	http://pekwm.org/projects/pekwm/files/%{name}-%{version}.tar.gz
# Source0-md5:	1f7f9ed32cc03f565a3ad30fd6045c1f
Source1:	%{name}.desktop
Source2:	%{name}-xsession.desktop
URL:		http://pekwm.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXrandr-devel
Conflicts:	filesystem < 3.0-20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11
%define		_deskdir	/usr/share/gnome/wm-properties
%define		_xdeskdir	%{_datadir}/xsessions

%description
pekwm is a small, fast, functional and flexible window manager.

%description -l pl.UTF-8
pekwm jest małym, szybkim, funkcjonalnym i elastycznym zarządcą okien.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-debug \
	--enable-harbour \
	--enable-image-jpeg \
	--enable-image-png \
	--enable-image-xpm \
	--enable-menus \
	--enable-shape \
	--enable-xft \
	--enable-xinerama \
	--enable-xrandr

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install\
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_deskdir},%{_xdeskdir}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_deskdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_xdeskdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/themes
%dir %{_datadir}/%{name}/scripts
%attr(755,root,root) %{_datadir}/%{name}/scripts/*
%{_deskdir}/%{name}.desktop
%{_xdeskdir}/%{name}.desktop
%{_mandir}/man1/%{name}.1*
