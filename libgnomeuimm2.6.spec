%define pkgname libgnomeuimm
%define major 1
%define api_version 2.6
%define libname_orig	%mklibname gnomeuimm %{api_version}
%define libname		%mklibname gnomeuimm %{api_version} %{major}
%define develname %mklibname -d gnomeuimm %{api_version}

Summary:	A C++ wrapper for GNOME UI library
Name:		%{pkgname}%{api_version}
Version:	2.28.0
Release:	6
License:	LGPLv2+
Group:		System/Libraries
URL:		http://gtkmm.sourceforge.net/
Source:		http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	pkgconfig(gnome-vfsmm-2.6)
BuildRequires:	pkgconfig(gconfmm-2.6)
BuildRequires:	pkgconfig(libgnomemm-2.6)
BuildRequires:	pkgconfig(libgnomecanvasmm-2.6)
BuildRequires:	pkgconfig(libglademm-2.4)
BuildRequires:	pkgconfig(expat)
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


%package	-n %{develname}
Summary:	Development files for libgnomeui C++ wrapper
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{pkgname}-devel = %{version}-%{release}

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
%configure2_5x --disable-static
%make

### Build doc
pushd docs/reference
  perl -pi -e 's/^(HAVE_DOT.*=) YES$/$1 NO/' Doxyfile
  make all
popd

%install
%makeinstall_std

%files -n %{libname}
%doc AUTHORS COPYING
%{_libdir}/libgnomeuimm-%{api_version}.so.%{major}*

%files -n %{develname}
%doc COPYING ChangeLog TODO
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{pkgname}-%{api_version}

%files doc
%doc docs/reference/html 

%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 2.28.0-4mdv2011.0
+ Revision: 661470
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 2.28.0-3mdv2011.0
+ Revision: 602556
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.28.0-2mdv2010.1
+ Revision: 520863
- rebuilt for 2010.1

* Mon Sep 21 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446587
- update to new version 2.28.0

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.26.0-2mdv2010.0
+ Revision: 425561
- rebuild

* Mon Mar 16 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 355981
- update to new version 2.26.0

* Mon Sep 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 286532
- new version
- update license

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Mar 09 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 182993
- new version

* Sun Feb 10 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.2-1mdv2008.1
+ Revision: 164909
- new version

* Mon Jan 28 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.1-1mdv2008.1
+ Revision: 159486
- new version

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 2.20.0-2mdv2008.1
+ Revision: 150650
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Sep 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 85544
- new version
- new devel name
- bump deps


* Sat Mar 10 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.0-1mdv2007.1
+ Revision: 140352
- new version

* Tue Jan 02 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.0-2mdv2007.1
+ Revision: 103079
- Import libgnomeuimm2.6

* Tue Jan 02 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.0-2mdv2007.1
- Rebuild

* Wed Aug 23 2006 Götz Waschk <waschk@mandriva.org> 2.16.0-1mdv2007.0
- New release 2.16.0

* Tue Aug 08 2006 Götz Waschk <waschk@mandriva.org> 2.14.0-3mdv2007.0
- fix buildrequires

* Wed Aug 02 2006 Frederic Crozat <fcrozat@mandriva.com> 2.14.0-2mdv2007.0
- Rebuild with latest dbus

* Tue Apr 11 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.0-1mdk
- New release 2.14.0
- use mkrel

* Sun Oct 09 2005 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.0-1mdk
- New release 2.12.0

* Tue May 10 2005 Götz Waschk <waschk@mandriva.org> 2.10.0-2mdk
- fix devel provides

* Mon Mar 07 2005 Götz Waschk <waschk@linux-mandrake.com> 2.10.0-1mdk
- source URL
- New release 2.10.0

* Thu Jan 06 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.0-2mdk 
- Rebuild with latest howl

* Wed Nov 10 2004 Götz Waschk <waschk@linux-mandrake.com> 2.8.0-1mdk
- requires new libgnomeui
- fix source URL
- New release 2.8.0

* Tue Jul 06 2004 Abel Cheung <deaddog@deaddog.org> 2.6.0-2mdk
- Rebuild with new g++
- Reenable libtoolize

* Fri Apr 30 2004 Abel Cheung <deaddog@deaddog.org> 2.6.0-1mdk
- New major release

* Fri Apr 30 2004 Abel Cheung <deaddog@deaddog.org> 2.0.0-3mdk
- Rebuild
- Split documentation

