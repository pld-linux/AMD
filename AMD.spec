Summary:	AMD: approximate minimum degree
Name:		AMD
Version:	2.2.0
Release:	2
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
AMD is a set of routines for ordering a sparse matrix prior
to Cholesky factorization (or for LU factorization with
diagonal pivoting). There are versions in both C and Fortran.
A MATLAB interface is provided.
Note that this software has nothing to do with AMD the company.

%package devel
Summary:	Header files for amd library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki amd
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	UFconfig

%description devel
Header files for amd library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki amd.

%package static
Summary:	Static amd library
Summary(pl.UTF-8):	Statyczna biblioteka amd
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static amd library.

%description static -l pl.UTF-8
Statyczna biblioteka amd.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	F77="gfortran" \
	CFLAGS="%{rpmcflags} -fPIC" \
	libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}

%{__make} -C Lib install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

install Include/* $RPM_BUILD_ROOT%{_includedir}

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
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libamd.a
