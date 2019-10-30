%global enable_debugging 0
%define api 3.0
%define shortapi 3
%define major 0
%define libname %mklibname cinnamon-menu %shortapi %major
Summary:  A menu system for the Cinnamon project
Name: cinnamon-menus
Version: 4.2.0
Release: 1
License: LGPLv2+
Group: Graphical desktop/Other
URL: http://cinnamon.linuxmint.com 
# for git
Source0:       %{name}-%{version}.tar.gz
#SourceGet0: https://github.com/linuxmint/%{name}/archive/%{version}.tar.gz

BuildRequires: gnome-common
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig
BuildRequires: python-devel
BuildRequires: intltool
BuildRequires: gobject-introspection-devel

%description
cinnamon-menus is an implementation of the draft "Desktop
Menu Specification" from freedesktop.org. This package
also contains the Cinnamon menu layout configuration files,
.directory files and assorted menu related utility programs,
Python bindings, and a simple menu editor.

%package devel
Summary: Libraries and include files for the Cinnamon menu system
Group: Development/C
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %libname = %{version}-%{release}

%description devel
This package provides the necessary development libraries for
writing applications that use the Cinnamon menu system.

%package -n %libname
Summary: The cinnamon-menu library, a part of %{name}
Group: System/Libraries

%description -n %libname
The cinnamon-menu library, a part of %{name}\

%prep
%setup -q
sh autogen.sh

%build
%configure --disable-static \
   --enable-introspection \
%if %{enable_debugging}
   --enable-debug=yes
%else
   --enable-debug=no
%endif

make %{?_smp_mflags} V=1


%install
%{make_install}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS NEWS COPYING.LIB
%{_libdir}/girepository-1.0/CMenu-%{api}.typelib

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/cinnamon-menus-%{api}
%{_datadir}/gir-1.0/CMenu-%{api}.gir

%files -n %libname
%{_libdir}/libcinnamon-menu-%{shortapi}.so.%{major}*




%changelog
* Wed Dec 03 2014 tmb <tmb> 2.4.0-2.mga5
+ Revision: 800483
- bump rel past testing

* Sun Nov 23 2014 joequant <joequant> 2.4.0-1.mga5
+ Revision: 798405
- upgrade to 2.4

* Wed Oct 15 2014 umeabot <umeabot> 2.2.0-5.mga5
+ Revision: 742819
- Second Mageia 5 Mass Rebuild

* Thu Sep 18 2014 umeabot <umeabot> 2.2.0-4.mga5
+ Revision: 693610
- Rebuild to fix library dependencies

* Tue Sep 16 2014 umeabot <umeabot> 2.2.0-3.mga5
+ Revision: 678398
- Mageia 5 Mass Rebuild

* Wed May 14 2014 joequant <joequant> 2.2.0-2.mga5
+ Revision: 622768
- rebuild for cauldron

* Sat Apr 19 2014 joequant <joequant> 2.2.0-1.mga5
+ Revision: 616949
- imported package cinnamon-menus


* Sat Apr 12 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.0-1
- update to 2.2.0

* Sat Mar 22 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.1-0.1.gitc740513
- inital release

