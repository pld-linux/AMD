Summary:	AMD: Approximate Minimum Degree
Summary(pl.UTF-8):	AMD - przybliżony algorytm minimalnego stopnia
Name:		AMD
Version:	2.2.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.cise.ufl.edu/research/sparse/amd/%{name}-%{version}.tar.gz
# Source0-md5:	b3e9679ba20635ac4847f01c01d6e992
Patch0:		amd-ufconfig.patch
Patch1:		amd-shared.patch
URL:		http://www.cise.ufl.edu/research/sparse/amd/
BuildRequires:	UFconfig
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AMD is a set of routines for ordering a sparse matrix prior to
Cholesky factorization (or for LU factorization with diagonal
pivoting). There are versions in both C and Fortran. A MATLAB
interface is provided. Note that this software has nothing to do with
AMD the company.

%description -l pl.UTF-8
AMD to zbiór procedur do porządkowania macierzy rzadkich przed
rozkładem Cholesky'ego (lub do rozkładu LU z obrotami diagonalnymi).
Istnieją wersje zarówno w C, jak i Fortranie. Dostępny jest interfejs
do MATLAB-a. Uwaga: to oprogramowanie nie ma nic wspólnego z firmą
AMD.

%package devel
Summary:	Header files for AMD library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki AMD
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	UFconfig

%description devel
Header files for AMD library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki AMD.

%package static
Summary:	Static AMD library
Summary(pl.UTF-8):	Statyczna biblioteka AMD
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static AMD library.

%description static -l pl.UTF-8
Statyczna biblioteka AMD.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/amd

%{__make} -C Lib install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

install Include/* $RPM_BUILD_ROOT%{_includedir}/amd

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt Doc/{ChangeLog,License}
%attr(755,root,root) %{_libdir}/libamd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libamd.so.0

%files devel
%defattr(644,root,root,755)
%doc Doc/AMD_UserGuide.pdf
%attr(755,root,root) %{_libdir}/libamd.so
%{_libdir}/libamd.la
%{_includedir}/amd

%files static
%defattr(644,root,root,755)
%{_libdir}/libamd.a
