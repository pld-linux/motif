#
# WARNING: BETA versions of motif/openmotif are using higher soname
# than STABLE one so please don't use beta versions here because
# when stable version somes out everything would need to be recompiled
# using ,,stable soname''. Check out CURRENT= in configure.{in,ac}.
#
Summary:	Motif toolkit
Summary(pl.UTF-8):	Toolkit Motif
Name:		motif
Version:	2.3.4
Release:	5
License:	LGPL v2.1
Group:		X11/Libraries
Source0:	http://downloads.sourceforge.net/motif/%{name}-%{version}-src.tgz
# Source0-md5:	612bb8127d0d31da6e5474edf8a5c247
Source2:	mwmrc
Source5:	mwm-xsession.desktop
Source6:	ac_find_%{name}.m4
Patch0:		%{name}-makedepend.patch
Patch1:		%{name}-mwmrc.patch
Patch2:		%{name}-bison.patch
Patch3:		%{name}-freetype.patch
Patch4:		%{name}-parbuild.patch
Patch5:		format-security.patch
URL:		http://motif.ics.com/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 2:1.4.0
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-data-xbitmaps
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXp-devel
BuildRequires:	xorg-lib-libXt-devel
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	lesstif
Obsoletes:	openmotif < 2.3.4-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing

%define		xbitmapsdir	%{_includedir}/X11/bitmaps
%define		xlibdir		%{_libdir}/X11

%description
Motif is the user interface standart in the Enterprise for
applications that run on UNIX platforms for Sun, HP, IBM, Compaq, SGI,
and others.

%description -l pl.UTF-8
Motif jest standardem wyglądu interfejsu graficznego dla aplikacji
działających w środowiskach UNIX takich jak Sun, HP, IBM, Compaq, SGI
i inne.

%package clients
Summary:	Motif clients
Summary(pl.UTF-8):	Motif - programy klienckie
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Obsoletes:	lesstif-clients
Obsoletes:	openmotif-clients < 2.3.4-1

%description clients
Motif clients: uil and xmbind.

%description clients -l pl.UTF-8
Programy klienckie dla Motifa: uil i xmbind.

%package libs
Summary:	Motif shared libraries
Summary(pl.UTF-8):	Biblioteki współdzielone Motifa
Group:		Libraries
Obsoletes:	openmotif-libs < 2.3.4-1

%description libs
Motif shared libraries.

%description libs -l pl.UTF-8
Biblioteki współdzielone Motifa.

%package devel
Summary:	Header files for Motif libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek Motif
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXft-devel
Requires:	xorg-lib-libXmu-devel
Requires:	xorg-lib-libXp-devel
Requires:	xorg-lib-libXt-devel
Obsoletes:	lesstif-devel
Obsoletes:	openmotif-devel < 2.3.4-1

%description devel
Header files for Motif libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Motif.

%package static
Summary:	Motif static libraries
Summary(pl.UTF-8):	Statyczne biblioteki Motifa
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	lesstif-static
Obsoletes:	openmotif-static < 2.3.4-1

%description static
Motif static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne Motifa.

%package demos
Summary:	Motif demos
Summary(pl.UTF-8):	Programy demonstracyjne do Motifa
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	openmotif-demos < 2.3.4-1

%description demos
Motif demos.

%description demos -l pl.UTF-8
Programy demonstracyjne do Motifa.

%package mwm
Summary:	Motif window manager
Summary(pl.UTF-8):	Motifowy zarządca okien
Group:		X11/Window Managers
Requires:	%{name} = %{version}-%{release}
Obsoletes:	lesstif-mwm
Obsoletes:	openmotif-mwm < 2.3.4-1

%description mwm
A BETA release of mwm. It is derived from fvwm, with a new parser that
understands mwmrc syntax, and a general understanding of Mwm
resources.

%description mwm -l pl.UTF-8
Wersja BETA mwm. Pochodzi z fvwm, ma nowy parser rozumiejący składnię
mwmrc oraz zasoby Mwm.

%package compat
Summary:	Fake Motif compat libraries
Summary(pl.UTF-8):	Dowiązania udające biblioteki kompatybilności Motif
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}
%ifarch %{x8664} ia64 ppc64 s390x sparc64
Provides:	libXm.so.1()(64bit)
Provides:	libXm.so.2()(64bit)
Provides:	libXm.so.3()(64bit)
%else
Provides:	libXm.so.1
Provides:	libXm.so.2
Provides:	libXm.so.3
%endif

%description compat
Fake Motif/OpenMotif compat libraries (symlinks to current libXm
library, _some_ old programs may work with them).

%description compat -l pl.UTF-8
Dowiązania udające biblioteki kompatybilności Motif/OpenMotif
(dowiązania symboliczne do nowej wersji biblioteki libXm, _niektóre_
stare programy mogą z nimi działać).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%{__libtoolize}
%{__aclocal} -I .
%{__autoconf}
%{__autoheader}
%{__automake}
%{__autoconf}

%configure \
	--enable-shared \
	--enable-static \
	--enable-themes \
	--enable-xft \
	--enable-jpeg \
	--enable-png \
	--with-fontconfig-config="pkg-config fontconfig"

%{__make} clean
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/motif,%{_datadir}/xsessions} \
	$RPM_BUILD_ROOT{/etc/X11/mwm,%{_aclocaldir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	bmdir=%{xbitmapsdir} \
	bindir=%{_bindir} \
	binddir=%{xlibdir}/bindings

cd demos
# breaks -bi --short-circuit !
%{__make} clean
cp -a * $RPM_BUILD_ROOT%{_examplesdir}/motif
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/Xm
cd ..
mv -f $RPM_BUILD_ROOT%{_bindir}/{,motif-}column
mv -f $RPM_BUILD_ROOT%{_bindir}/{,motif-}tree

install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/X11/mwm/system.mwmrc

install %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/xsessions/mwm.desktop
install %{SOURCE6} $RPM_BUILD_ROOT%{_aclocaldir}

cd $RPM_BUILD_ROOT%{_libdir}
ln -sf libXm.so.*.*.* libXm.so.3
ln -sf libXm.so.*.*.* libXm.so.2
ln -sf libXm.so.*.*.* libXm.so.1

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs	-p /sbin/ldconfig
%postun	libs	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc BUGREPORT ChangeLog README RELNOTES
%{xbitmapsdir}/xm_*
%{xlibdir}/bindings

%files clients
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uil
%attr(755,root,root) %{_bindir}/xmbind
%{_mandir}/man1/uil.1*
%{_mandir}/man1/xmbind.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libMrm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libMrm.so.4
%attr(755,root,root) %{_libdir}/libUil.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libUil.so.4
%attr(755,root,root) %{_libdir}/libXm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXm.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libMrm.so
%attr(755,root,root) %{_libdir}/libUil.so
%attr(755,root,root) %{_libdir}/libXm.so
%{_libdir}/libMrm.la
%{_libdir}/libUil.la
%{_libdir}/libXm.la
%{_includedir}/Mrm
%{_includedir}/Xm
%{_includedir}/uil
%{_mandir}/man3/ApplicationShell.3*
%{_mandir}/man3/Composite.3*
%{_mandir}/man3/Constraint.3*
%{_mandir}/man3/Core.3*
%{_mandir}/man3/Mrm*.3*
%{_mandir}/man3/Object.3*
%{_mandir}/man3/OverrideShell.3*
%{_mandir}/man3/RectObj.3*
%{_mandir}/man3/Shell.3*
%{_mandir}/man3/TopLevelShell.3*
%{_mandir}/man3/TransientShell.3*
%{_mandir}/man3/Uil.3*
%{_mandir}/man3/UilDumpSymbolTable.3*
%{_mandir}/man3/VendorShell.3*
%{_mandir}/man3/VirtualBindings.3*
%{_mandir}/man3/WMShell.3*
%{_mandir}/man3/Xm*.3*
# should be man7?
%{_mandir}/man5/Traits.5*
%{_mandir}/man5/UIL.5*
%{_mandir}/man5/WML.5*
%{_aclocaldir}/ac_find_motif.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libMrm.a
%{_libdir}/libUil.a
%{_libdir}/libXm.a

%files demos
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/DNDDemo
%attr(755,root,root) %{_bindir}/airport
%attr(755,root,root) %{_bindir}/autopopups
%attr(755,root,root) %{_bindir}/bboxdemo
%attr(755,root,root) %{_bindir}/colordemo
%attr(755,root,root) %{_bindir}/motif-column
%attr(755,root,root) %{_bindir}/combo
%attr(755,root,root) %{_bindir}/draw
%attr(755,root,root) %{_bindir}/earth
%attr(755,root,root) %{_bindir}/ext18list
%attr(755,root,root) %{_bindir}/filemanager
%attr(755,root,root) %{_bindir}/fileview
%attr(755,root,root) %{_bindir}/fontsel
%attr(755,root,root) %{_bindir}/getsubres
%attr(755,root,root) %{_bindir}/helloint
%attr(755,root,root) %{_bindir}/hellomotif
%attr(755,root,root) %{_bindir}/i18ninput
%attr(755,root,root) %{_bindir}/iconbuttondemo
%attr(755,root,root) %{_bindir}/outline
%attr(755,root,root) %{_bindir}/paned
%attr(755,root,root) %{_bindir}/panner
%attr(755,root,root) %{_bindir}/periodic
%attr(755,root,root) %{_bindir}/piano
%attr(755,root,root) %{_bindir}/sampler2_0
%attr(755,root,root) %{_bindir}/setDate
%attr(755,root,root) %{_bindir}/simpleDemo
%attr(755,root,root) %{_bindir}/simpledrop
%attr(755,root,root) %{_bindir}/tabstack
%attr(755,root,root) %{_bindir}/todo
%attr(755,root,root) %{_bindir}/tooltips
%attr(755,root,root) %{_bindir}/motif-tree
%attr(755,root,root) %{_bindir}/wsm
%attr(755,root,root) %{_bindir}/xmanimate
%{_examplesdir}/motif

%files mwm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mwm
%dir %{_sysconfdir}/X11/mwm
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/mwm/system.mwmrc
%{_datadir}/xsessions/mwm.desktop
%{_mandir}/man1/mwm.1*
# should be man5
%{_mandir}/man4/mwmrc.4*

%files compat
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXm.so.1
%attr(755,root,root) %{_libdir}/libXm.so.2
%attr(755,root,root) %{_libdir}/libXm.so.3
