Summary:	OpenMotif
Summary(pl):	OpenMotif
Name:		openmotif
Version:	2.2.2
Release:	0.7
License:	Open Group Public License
Group:		X11/Libraries
Source0:	ftp://openmotif.opengroup.org/pub/openmotif/R2.2/tars/%{name}-%{version}.tgz
# Source0-md5: c5953e0fa08f79644e7bef9da218bb4b
#Source1:	%{name}-%{version}-icsextra.tgz
Source2:	mwmrc
Source3:	mwm.RunWM
Source4:	mwm.wm_style
Patch0:		%{name}-makedepend.patch
#Patch1:		%{name}-build.patch
#Patch2:		%{name}-mwm.patch
#Patch3:		%{name}-mwmrc.patch
Patch4:		%{name}-ppc_fix.patch
Patch5:		%{name}-ac-fixes.patch
Patch6:		%{name}-am-demos.patch
Patch7:		%{name}-am-uil.patch
Patch8:		%{name}-am-animate.patch
BuildRequires:	XFree86
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	byacc
BuildRequires:	flex
BuildRequires:	libtool
Provides:	motif = 2.2
# Not restricted, lesstif provided library version 1.2
# OpenMotif provide library version 2.1
#Obsoletes:	lesstif
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Motif is the user interface standart in the Enterprise for
applications that run on UNIX platforms for Sun, HP, IBM, Compaq, SGI,
and others.

%description -l pl
Motif jest standardem wygl�du interfejsu graficznego dla aplikacji
dzia�aj�cych w �rodowiskach UNIX takich jak Sun, HP, IBM, Compaq, SGI
i inne.

%package clients
Summary:	OpenMotif clients
Summary(pl):	OpenMotif - programy klienckie
Group:		X11/Applications
Requires:	%{name} = %{version}
Obsoletes:	lesstif-clients

%description clients
Uil and xmbind.

%description clients -l pl
uil i xmbind.

%package devel
Summary:	OpenMotif devel
Summary(pl):	Pliki nag��wkowe OpenMotif
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Provides:	motif-devel = 2.1
Obsoletes:	lesstif-devel

%description devel
Header files for OpenMotif.

%description devel -l pl
Pliki nag��wkowe dla bibliotek OpenMotif.

%package static
Summary:	OpenMotif static
Summary(pl):	Statyczne biblioteki OpenMotif
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}
Provides:	motif-static
Obsoletes:	lesstif-static

%description static
OpenMotif static libraries.

%description static -l pl
Biblioteki statyczne OpenMotif.

%package demos
Summary:	OpenMotif demos
Summary(pl):	Programy demonstracyjne do OpenMotif
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description demos
OpenMotif demos.

%description demos -l pl
Programy demonstracyjne do OpenMotif.

%package mwm
Summary:	Motif window manager
Summary(pl):	Motifowy zarz�dca okien
Group:		X11/Window Managers
Requires:	%{name} = %{version}
Requires:	wmconfig >= 0.9.9-5
Requires:	xinitrc >= 3.0
Obsoletes:	lesstif-mwm

%description mwm
A BETA release of mwm. It is derived from fvwm, with a new parser that
understands mwmrc syntax, and a general understanding of Mwm
resources.

%description mwm -l pl
Wersja BETA mwm. Pochodzi z fvwm, ma nowy parser rozumiej�cy sk�adni�
mwmrc oraz zasoby Mwm.

%prep
%setup -q
#-b 1
#rm -f config/cf/host.def
%patch0 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
#%patch1 -p1
#%patch2 -p1
#%patch3 -p1

#touch clients/mwm/mwm.man

#mkdir -p imports/x11
#cd imports/x11
#ln -sf /usr/X11R6/include .
#ln -sf /usr/X11R6/lib .
#cd ../../config/cf
#mkdir OPENGROUP
#mv -f *.tmpl *.rules *.def OPENGROUP
#ln -sf /usr/X11R6/lib/X11/config/* .
#rm -f Motif.tmpl Motif.rules host.def
#mv -f OPENGROUP/{Motif.tmpl,Motif.rules,host.def} .

#%ifarch ppc
#rm linux.cf
#%patch4 -p3
#%endif

%build
rm -f missing
%{__libtoolize}
#%%{__gettextize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make} clean
%{__make}

#%%{__make} World \
#	IMAKE_DEFINES="-DYaccCmd=yacc" \
#	BOOTSTRAPCFLAGS="%{rpmcflags}" \
#	CDEBUGFLAGS="" CCOPTIONS="%{rpmcflags}" \
#	CXXDEBUGFLAGS="" CXXOPTIONS="%{rpmcflags}" \
#	RAWCPP="/lib/cpp"

# workaround - don't let rebuild onHelp with wrong options during %install
#touch demos/lib/Xmd/onHelp.o demos/lib/Xmd/onHelp

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/motif,/etc/{sysconfig/wmstyle,X11/mwm}}

%{__make} install DESTDIR="$RPM_BUILD_ROOT"
#	INSTBINFLAGS="-m 755" \
#	INSTPGMFLAGS="-m 755" \
#	RAWCPP="/lib/cpp" \
#	install install.man

#cp -a doc/man/* $RPM_BUILD_ROOT%{_mandir}
#mv -f $RPM_BUILD_ROOT%{_mandir}/man1/animate.1x \
#$RPM_BUILD_ROOT%{_mandir}/man1/xmanimate.1x

#
cd demos
%{__make} clean
cp -a * $RPM_BUILD_ROOT%{_examplesdir}/motif
cd ..

#
#(cd doc/ps
#find -name \*.Z -print | xargs uncompress
#find -name \*.ps -print | xargs gzip -9nf)
#
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/X11/mwm/system.mwmrc

install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/wmstyle/mwm.sh
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/wmstyle/mwm.names

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE COPYRIGHT.MOTIF OPENBUGS RELNOTES
#%dir %{_libdir}/X11/uid
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_includedir}/X11/bitmaps/*
%{_libdir}/X11/bindings

%files clients
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uil*
%attr(755,root,root) %{_bindir}/xmbind
%{_mandir}/man1/uil.1*
%{_mandir}/man1/xmbind.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/Mrm
%{_includedir}/Xm
%{_includedir}/uil
%{_mandir}/man3/*
%{_mandir}/man5/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files demos
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/DNDDemo
%attr(755,root,root) %{_bindir}/airport
%attr(755,root,root) %{_bindir}/autopopups
#%attr(755,root,root) %{_bindir}/dainput
#%attr(755,root,root) %{_bindir}/dogs
%attr(755,root,root) %{_bindir}/draw
%attr(755,root,root) %{_bindir}/earth
#%attr(755,root,root) %{_bindir}/exm_in_c
#%attr(755,root,root) %{_bindir}/exm_in_uil
%attr(755,root,root) %{_bindir}/filemanager
%attr(755,root,root) %{_bindir}/fileview
%attr(755,root,root) %{_bindir}/getsubres
%attr(755,root,root) %{_bindir}/helloint
%attr(755,root,root) %{_bindir}/hellomotif
%attr(755,root,root) %{_bindir}/i18ninput
#%attr(755,root,root) %{_bindir}/motifshell
#%attr(755,root,root) %{_bindir}/onHelp
%attr(755,root,root) %{_bindir}/panner
%attr(755,root,root) %{_bindir}/periodic
%attr(755,root,root) %{_bindir}/piano
%attr(755,root,root) %{_bindir}/sampler2_0
%attr(755,root,root) %{_bindir}/setDate
#%attr(755,root,root) %{_bindir}/simpleDemo
%attr(755,root,root) %{_bindir}/simpledrop
%attr(755,root,root) %{_bindir}/todo
%attr(755,root,root) %{_bindir}/wsm
%attr(755,root,root) %{_bindir}/xmanimate
#%attr(755,root,root) %{_bindir}/xmapdef
#%attr(755,root,root) %{_bindir}/xmfonts
#%attr(755,root,root) %{_bindir}/xmforc
#%attr(755,root,root) %{_bindir}/xmform
#%%{_libdir}/X11/app-defaults/Fileview
#%%{_libdir}/X11/app-defaults/Xmd*
#%%{_libdir}/X11/uid/*
#%%{_mandir}/man1/DNDDemo.1*
#%%{_mandir}/man1/autopopups.1*
#%%{_mandir}/man1/draw.1*
#%%{_mandir}/man1/earth.1*
#%%{_mandir}/man1/exm_in_c.1*
#%%{_mandir}/man1/exm_in_uil.1*
#%%{_mandir}/man1/filemanager.1*
#%%{_mandir}/man1/getsubres.1*
#%%{_mandir}/man1/helloint.1*
#%%{_mandir}/man1/i18ninput.1*
#%%{_mandir}/man1/panner.1*
#%%{_mandir}/man1/periodic.1*
#%%{_mandir}/man1/piano.1*
#%%{_mandir}/man1/sampler2_0.1*
#%%{_mandir}/man1/setDate.1*
#%%{_mandir}/man1/simpleDemo.1*
#%%{_mandir}/man1/simpledrop.1*
#%%{_mandir}/man1/todo.1*
#%%{_mandir}/man1/wsm.1*
#%%{_mandir}/man1/xmanimate.1*
%{_examplesdir}/motif

%files mwm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mwm
%dir %{_sysconfdir}/X11/mwm
%config %{_sysconfdir}/X11/mwm/*
%attr(755,root,root) /etc/sysconfig/wmstyle/*.sh
/etc/sysconfig/wmstyle/*.names
#%%{_libdir}/X11/app-defaults/Mwm
%{_mandir}/man1/mwm.1*
%{_mandir}/man4/*
