Summary:	micro bitmap font
Summary(pl.UTF-8):	Font bitmapowy micro
Name:		xorg-font-font-micro-misc
Version:	1.0.4
Release:	1
License:	Public Domain
Group:		Fonts
Source0:	https://xorg.freedesktop.org/releases/individual/font/font-micro-misc-%{version}.tar.xz
# Source0-md5:	ee3af8a93abc1695aeebb55bcd953a16
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.4
BuildRequires:	xorg-util-util-macros >= 1.20
BuildRequires:	xz
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
micro bitmap font.

%description -l pl.UTF-8
Font bitmapowy micro.

%prep
%setup -q -n font-micro-misc-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
%if "%{_gnu}" != "-gnux32"
	--build=%{_host} \
	--host=%{_host} \
%endif
	--with-fontdir=%{_fontsdir}/misc

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst misc

%postun
fontpostinst misc

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%{_fontsdir}/misc/micro.pcf.gz
