Summary:	RVM library
Name:		rvm
Version:	1.1
Release:	1
License:	GPL
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
BuildRequires:	lwp-devel
Source:		ftp://ftp.coda.cs.cmu.edu/pub/coda/src/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The RVM persistent recoverable memory library. The RVM library is used by
the Coda distributed filesystem.

%package tools
Summary:	RVM tools
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description tools
Userspace tools to initialize and manipulate RVM log and data segments.
The RVM library is used by the Coda distributed filesystem.

%package devel
Summary:	RVM library development files
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Headers and libraries for developing programs using the RVM library.
The RVM library is used by the Coda distributed filesystem.

%package static
Summary:	Static RVM libraries
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libraries for developing programs using the RVM library.
The RVM library is used by the Coda distributed filesystem.

%prep
%setup -q

%build
%configure --prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(755,root,root,755)
%{_libdir}/librvm.so.1.0.0
%{_libdir}/librvmlwp.so.1.0.0
%{_libdir}/libseg.so.1.0.0
%{_libdir}/librds.so.1.0.0
%{_libdir}/librdslwp.so.1.0.0

%files tools
%defattr(755,root,root,755)
%{_sbindir}/rvmutl
%{_sbindir}/rdsinit

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/rvm/rvm.h
%{_includedir}/rvm/rvm_statistics.h
%{_includedir}/rvm/rvm_segment.h
%{_includedir}/rvm/rds.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
