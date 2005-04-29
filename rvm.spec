Summary:	RVM library
Summary(pl):	Biblioteka RVM
Name:		rvm
Version:	1.10
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	ftp://ftp.coda.cs.cmu.edu/pub/rvm/src/%{name}-%{version}.tar.gz
# Source0-md5:	284866164a3f016e944d1bd1854e23ba
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	lwp-devel
BuildRequires:	lwp-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The RVM persistent recoverable memory library. The RVM library is used
by the Coda distributed filesystem.

%description -l pl
Biblioteka RVM odzyskiwalnej pamiêci. Jest u¿ywana z systemem plików
CODA.

%package tools
Summary:	RVM tools
Summary(pl):	Narzêdzia RVM
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description tools
Userspace tools to initialize and manipulate RVM log and data
segments. The RVM library is used by the Coda distributed filesystem.

%description tools -l pl
Narzêdzia do inicjalizacji i manipulacji log'ami RVM oraz segmentami
danych. Biblioteka RVM jest u¿ywana z systemem plików CODA.

%package devel
Summary:	RVM library development files
Summary(pl):	Pliki developerskie biblioteki RVM
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Headers and libraries for developing programs using the RVM library.
The RVM library is used by the Coda distributed filesystem.

%description devel -l pl
Pliki nag³ówkowe oraz biblioteki do tworzenia programów u¿ywaj±cych
biblioteki RVM.

%package static
Summary:	Static RVM libraries
Summary(pl):	Statyczne biblioteki RVM
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries for developing programs using the RVM library. The
RVM library is used by the Coda distributed filesystem.

%description static -l pl
Statyczne biblioteki do tworzenia programów u¿ywaj±cych bibliotek RVM.

%prep
%setup -q

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

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
