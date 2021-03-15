%define api 3.0
%define shortapi 3
%define major 0
%define libname %mklibname cinnamon-menu %shortapi %major
Summary:  A menu system for the Cinnamon project
Name: cinnamon-menus
Version: 4.8.3
Release: 1
License: LGPLv2+
Group: Graphical desktop/Other
URL: http://cinnamon.linuxmint.com 
Source0:       https://github.com/linuxmint/cinnamon-menus/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: meson
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

%build
%meson -Denable_debug=false
%meson_build


%install
%meson_install
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
