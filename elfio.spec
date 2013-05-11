Summary:	ELF (Executable and Linkable Format) reader and producer implemented as a C++ library
Summary(pl.UTF-8):	Biblioteka C++ do odczytu i tworzenia plików w formacie ELF
Name:		elfio
Version:	2.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://downloads.sourceforge.net/elfio/%{name}-%{version}.tar.gz
# Source0-md5:	d370c4e4ff432626dba661f9a30ff2f1
URL:		http://elfio.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ELFIO is a C++ library for reading and generating files in the ELF
binary format. This library is unique and not based on any other
product. It is also platform independent. The library uses standard
ANSI C++ constructions and runs on a wide variety of architectures.

%description -l pl.UTF-8
ELFIO to biblioteka C++ do odczytu i tworzenia plików w formacie
binarnym ELF (Executable and Linkable Format). Biblioteka ta jest
unikalna, nie oparta na żadnym innym produkcie. Jest także niezależna
od platformy. Wykorzystuje standardowe konstrukcje ANSI C++ i działa
na wielu architekturach.

%package devel
Summary:	Development headers for programs using the elfio library
Summary(pl.UTF-8):	Pliki nagłówkowe dla programów wykorzystujących bibliotekę elfio
Group:		Development/Libraries
Requires:	libstdc++-devel
# doesn't require base (header-only library)

%description devel
This package contains the header files needed for developing programs
using the elfio library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe niezbędne do tworzenia programów
wykorzystujących bibliotekę elfio.

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
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/elfdump

%files devel
%defattr(644,root,root,755)
%doc doc/elfio.pdf
%{_includedir}/elfio
