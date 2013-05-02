Summary:	ELF (Executable and Linkable Format) reader and producer implemented as a C++ library
Name:		elfio
Version:	2.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://downloads.sourceforge.net/project/elfio/ELFIO-sources/ELFIO-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d370c4e4ff432626dba661f9a30ff2f1
URL:		http://elfio.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ELFIO is a C++ library for reading and generating files in the ELF
binary format. This library is unique and not based on any other
product. It is also platform independent. The library uses standard
ANSI C++ constructions and runs on a wide variety of architectures.

%package devel
Summary:	Development tools for programs using the elfio library
Group:		Development/Libraries

%description devel
This package contains the header files and libraries needed for
developing programs using the elfio library.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_bindir}/{tutorial,write_obj,writer}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/elfdump

%files devel
%defattr(644,root,root,755)
%doc doc/elfio.pdf
%{_includedir}/elfio
