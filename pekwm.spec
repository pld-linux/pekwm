Summary:	pekwm - based on the aewm++ window manager
Summary(pl):	pekwm - bazuj�cy na aewm++ zarz�dc� okien
Name:		pekwm
Version:	0.1.3
Release:	1
License:	GPL v2
Group:		X11/Window Managers
Source0:	http://pekwm.org/files/source/%{name}-%{version}.tar.bz2
# Source0-md5:	c0bd31ae08fa0067f6a6584270403675
Source1:	%{name}.desktop
Source2:	%{name}-xsession.desktop
Patch0:		%{name}-fixmandir.patch
URL:		http://pekwm.org/
Buildrequires:	XFree86-devel
Buildrequires:	XFree86-libs
BuildRequires:  libstdc++-devel
Requires:       xinitrc-ng
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define  _sysconfdir	/etc/X11
%define	 _deskdir	/usr/share/wm-propertis
%define	 _xdeskdir	%{_datadir}/xsession
%bcond_with xinerama

%description
pekwm is a small, fast, functional and flexible window manager.

%description -l pl
pekwm jest ma�ym, szybkim, funkcjonalnym i elastycznym zarz�dc� okien.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--enable-shape \
	--disable-debug \
	--enable-menus \
	--enable-keygrabber \
	--enable-harbour \
	%{?with_xinerama: --enable-xinerama} \
	--disable-pcre 

%{__make}

%install
%{__make} install\
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_deskdir},%{_xdeskdir}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_deskdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_xdeskdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README README.aewm++ TODO docs/pekwmdocs.txt docs/pekwmdocs.html
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/*
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/%{name}/themes/
%dir %{_datadir}/%{name}/scripts
%attr(755,root,root) %{_datadir}/%{name}/scripts/*
%{_deskdir}/%{name}.desktop
%{_xdeskdir}/%{name}.desktop
