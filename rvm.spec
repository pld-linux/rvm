Summary:	RVM library
Summary(pl.UTF-8):	Biblioteka RVM
Name:		rvm
Version:	1.17
Release:	0.1
License:	GPL
Group:		Development/Libraries
Source0:	ftp://ftp.coda.cs.cmu.edu/pub/rvm/src/%{name}-%{version}.tar.gz
# Source0-md5:	208486ed214c254280a6c23f8f5599bd
Patch0:		%{name}-configure.patch
URL:		http://www.cs.cmu.edu/afs/cs/project/coda-www/ResearchWebPages/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	lwp-devel
BuildRequires:	lwp-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The RVM persistent recoverable memory library. The RVM library is used
by the Coda distributed filesystem.

%description -l pl.UTF-8
Biblioteka RVM odzyskiwalnej pamięci. Jest używana z systemem plików
CODA.

%package tools
Summary:	RVM tools
Summary(pl.UTF-8):	Narzędzia RVM
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description tools
Userspace tools to initialize and manipulate RVM log and data
segments. The RVM library is used by the Coda distributed filesystem.

%description tools -l pl.UTF-8
Narzędzia do inicjalizacji i manipulacji log'ami RVM oraz segmentami
danych. Biblioteka RVM jest używana z systemem plików CODA.

%package devel
Summary:	RVM library development files
Summary(pl.UTF-8):	Pliki developerskie biblioteki RVM
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Headers and libraries for developing programs using the RVM library.
The RVM library is used by the Coda distributed filesystem.

%description devel -l pl.UTF-8
Pliki nagłówkowe oraz biblioteki do tworzenia programów używających
biblioteki RVM.

%package static
Summary:	Static RVM libraries
Summary(pl.UTF-8):	Statyczne biblioteki RVM
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries for developing programs using the RVM library. The
RVM library is used by the Coda distributed filesystem.

%description static -l pl.UTF-8
Statyczne biblioteki do tworzenia programów używających bibliotek RVM.

%prep
%setup -q
%patch -P0 -p1

%build
rm -f missing
touch ChangeLog AUTHORS README
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make} \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/rvmutl
%attr(755,root,root) %{_sbindir}/rdsinit

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/rvm
%{_pkgconfigdir}/rvmlwp.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
