Summary:	AMD: Approximate Minimum Degree
Name:		AMD
Version:	2.2.0
Release:	3
License:	LGPL
Group:		Libraries
Source0:	http://www.cise.ufl.edu/research/sparse/amd/%{name}-%{version}.tar.gz
# Source0-md5:	f81fcae945de82864035b03ee20a8d2b
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
	F77="gfortran" \
	CFLAGS="%{rpmcflags} -fPIC" \
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
%doc README.txt
%attr(755,root,root) %{_libdir}/libamd.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libamd.so
%{_libdir}/libamd.la
%{_includedir}/amd

%files static
%defattr(644,root,root,755)
%{_libdir}/libamd.a
