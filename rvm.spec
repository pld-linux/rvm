Summary:	RVM library
Name:		rvm
Version:	1.6
Release:	1
License:	GPL
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Source0:	ftp://ftp.coda.cs.cmu.edu/pub/rvm/src/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	lwp-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The RVM persistent recoverable memory library. The RVM library is used
by the Coda distributed filesystem.

%package tools
Summary:	RVM tools
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description tools
Userspace tools to initialize and manipulate RVM log and data
segments. The RVM library is used by the Coda distributed filesystem.

%package devel
Summary:	RVM library development files
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Headers and libraries for developing programs using the RVM library.
The RVM library is used by the Coda distributed filesystem.

%package static
Summary:	Static RVM libraries
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libraries for developing programs using the RVM library. The
RVM library is used by the Coda distributed filesystem.

%prep
%setup -q

%build
rm -f missing
touch ChangeLog AUTHORS README
autoheader
aclocal
libtoolize --copy --force
autoconf
automake -a -c
%configure
%{__make} OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/rvmutl
%attr(755,root,root) %{_sbindir}/rdsinit

%files devel
%defattr(644,root,root,755)
%doc NEWS.gz
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/rvm

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
