%define version 2.20.0
%define release %mkrel 1

%define libgnomemm_version 2.14.0
%define libgnomecanvasmm_version 2.6.0
%define gconfmm_version 2.6.0
%define gnomevfsmm_version 2.6.0
%define libglademm_version 2.4.0

%define pkgname libgnomeuimm
%define major 1
%define api_version 2.6
%define libname_orig	%mklibname gnomeuimm %{api_version}
%define libname		%mklibname gnomeuimm %{api_version} %{major}
%define develname %mklibname -d gnomeuimm %{api_version}

Summary:	A C++ wrapper for GNOME UI library
Name:		%{pkgname}%{api_version}
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		System/Libraries
URL:		http://gtkmm.sourceforge.net/
Source:		http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.bz2
BuildRequires:	libgnomeui2-devel >= 2.7.1
BuildRequires:	gnome-vfsmm2.6-devel >= %{gnomevfsmm_version}
BuildRequires:	gconfmm2.6-devel >= %{gconfmm_version}
BuildRequires:	libgnomemm2.6-devel >= %{libgnomemm_version}
BuildRequires:	libgnomecanvasmm2.6-devel >= %{libgnomecanvasmm_version}
BuildRequires:	libglademm2.4-devel >= %{libglademm_version}
BuildRequires:	libexpat-devel
BuildRequires:	doxygen

%description
This library provides a C++ wrapper for GNOME UI library.
It is a subpackage of the gnomemm project, which provides C++ binding
of various GNOME libraries.


%package	-n %{libname}
Summary:	A C++ wrapper for GNOME UI library
Group:		System/Libraries
Provides:	%{libname_orig} = %{version}-%{release}
Provides:	%{pkgname} = %{version}-%{release}

%description	-n %{libname}
This library provides a C++ wrapper for GNOME UI library.
It is a subpackage of the gnomemm project, which provides C++ binding
of various GNOME libraries.


%package	-n %develname
Summary:	Development files for libgnomeui C++ wrapper
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{pkgname}-devel = %{version}-%{release}
Obsoletes: %mklibname -d gnomeuimm %api_version 1

%description	-n %develname
This package contains all necessary files, including libraries and headers,
that C++ programmers will need to develop applications which use
%{pkgname}, the C++ interface to libgnomeui.

It is necessary when compiling applications which use %{pkgname} as well.


%package	doc
Summary:	Documentation of %{pkgname} library
Group:		Books/Other

%description	doc
This package provides API documentation of %{pkgname} library.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%configure2_5x --enable-static
%make

### Build doc
pushd docs/reference
  perl -pi -e 's/^(HAVE_DOT.*=) YES$/$1 NO/' Doxyfile
  make all
popd

%install
rm -rf %{buildroot}
%makeinstall_std
find %buildroot -name \*.la|xargs chmod 644

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}


%files -n %{libname}
%defattr(-, root, root)
%doc AUTHORS COPYING
%{_libdir}/libgnomeuimm-%{api_version}.so.%{major}*

%files -n %develname
%defattr(-, root, root)
%doc COPYING ChangeLog TODO
%{_includedir}/*
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{pkgname}-%{api_version}

%files doc
%defattr(-, root, root)
%doc docs/reference/html 


