Summary:	micro bitmap font
Summary(pl.UTF-8):	Font bitmapowy micro
Name:		xorg-font-font-micro-misc
Version:	1.0.1
Release:	1
License:	Public Domain
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-micro-misc-%{version}.tar.bz2
# Source0-md5:	6350117efebe340f33e818f4a33e4e4b
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
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
	--build=%{_host_platform} \
	--host=%{_host_platform} \
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
%doc COPYING ChangeLog
%{_fontsdir}/misc/micro.pcf.gz
