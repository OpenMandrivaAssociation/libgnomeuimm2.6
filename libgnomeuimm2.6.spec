%define url_ver %(echo %{version}|cut -d. -f1,2)

%define pkgname	libgnomeuimm
%define api	2.6
%define major	1
%define libname	%mklibname gnomeuimm %{api} %{major}
%define devname	%mklibname -d gnomeuimm %{api}

Summary:	A C++ wrapper for GNOME UI library
Name:		%{pkgname}%{api}
Version:	2.28.0
Release:	7
License:	LGPLv2+
Group:		System/Libraries
Url:		http://gtkmm.sourceforge.net/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgnomeuimm/%{url_ver}/%{pkgname}-%{version}.tar.bz2

BuildRequires:	doxygen
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(gconfmm-2.6)
BuildRequires:	pkgconfig(gnome-vfsmm-2.6)
BuildRequires:	pkgconfig(libglademm-2.4)
BuildRequires:	pkgconfig(libgnomecanvasmm-2.6)
BuildRequires:	pkgconfig(libgnomemm-2.6)
BuildRequires:	pkgconfig(libgnomeui-2.0)

%description
This library provides a C++ wrapper for GNOME UI library.
It is a subpackage of the gnomemm project, which provides C++ binding
of various GNOME libraries.


%package	-n %{libname}
Summary:	A C++ wrapper for GNOME UI library
Group:		System/Libraries
Provides:	%{pkgname} = %{version}-%{release}

%description	-n %{libname}
This library provides a C++ wrapper for GNOME UI library.
It is a subpackage of the gnomemm project, which provides C++ binding
of various GNOME libraries.


%package	-n %{devname}
Summary:	Development files for libgnomeui C++ wrapper
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description	-n %{devname}
This package contains all necessary files, including libraries and headers,
that C++ programmers will need to develop applications which use
%{pkgname}, the C++ interface to libgnomeui.

%package	doc
Summary:	Documentation of %{pkgname} library
Group:		Books/Other

%description	doc
This package provides API documentation of %{pkgname} library.

%prep
%setup -qn %{pkgname}-%{version}

%build
%configure2_5x --disable-static
%make

### Build doc
pushd docs/reference
  sed -i -e 's/^(HAVE_DOT.*=) YES$/$1 NO/' Doxyfile
  make all
popd

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libgnomeuimm-%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING ChangeLog TODO
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{pkgname}-%{api}

%files doc
%doc docs/reference/html 

