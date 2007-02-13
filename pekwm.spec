#
# Conditional build
%bcond_with	xinerama	# build with xinerama extension
#
Summary:	pekwm - based on the aewm++ window manager
Summary(pl.UTF-8):	pekwm - zarządca okien oparty na aewm++
Name:		pekwm
Version:	0.1.4
%define	_pre	pre2
#define _pre	%nil
Release:	0.%{_pre}.1
License:	GPL v2
Group:		X11/Window Managers
Source0:	http://pekwm.org/files/%{name}-%{version}%{_pre}.tar.bz2
# Source0-md5:	a5aae71550cb8ace2bc4db423d67532a
Source1:	%{name}.desktop
Source2:	%{name}-xsession.desktop
#Patch0:		%{name}-fixmandir.patch
URL:		http://pekwm.org/
BuildRequires:	XFree86-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11
%define		_deskdir	/usr/share/wm-properties
%define		_xdeskdir	%{_datadir}/xsession

%description
pekwm is a small, fast, functional and flexible window manager.

%description -l pl.UTF-8
pekwm jest małym, szybkim, funkcjonalnym i elastycznym zarządcą okien.

%prep
%setup -q -n %{name}-%{version}%{_pre}
#patch0 -p1

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
#{_mandir}/man1/%{name}.1*
