%define gitcmmt 4ed577d

Name:		sfarkxtc
Version:	3.0
Release:	3
Summary:	Command line tool for decompressing sfArk sound fonts
License:	GPLv3
Group:		System/Libraries
URL:		https://github.com/raboof/sfarkxtc
Source0:	https://github.com/raboof/sfarkxtc/archive/master.tar.gz
BuildRequires:	pkgconfig(zlib)
BuildRequires:	sfarklib-devel

%description
Command line tool for decompressing sfArk sound fonts

%prep
%setup -qn raboof-%{name}-%{gitcmmt}

%build
%{__cc} %{optflags} -o %{name} %{name}.cpp -lz -lsfark

%install
mkdir -p %{buildroot}%{_bindir}
cp -a %{name} %{buildroot}%{_bindir}/

%files
%{_bindir}/%{name}
