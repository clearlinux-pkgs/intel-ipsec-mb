#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : intel-ipsec-mb
Version  : 1.2
Release  : 9
URL      : https://github.com/intel/intel-ipsec-mb/archive/v1.2/intel-ipsec-mb-1.2.tar.gz
Source0  : https://github.com/intel/intel-ipsec-mb/archive/v1.2/intel-ipsec-mb-1.2.tar.gz
Summary  : IPSEC cryptography library optimized for Intel Architecture
Group    : Development/Tools
License  : BSD-3-Clause
Requires: intel-ipsec-mb-lib = %{version}-%{release}
Requires: intel-ipsec-mb-license = %{version}-%{release}
BuildRequires : llvm
BuildRequires : llvm-dev
BuildRequires : nasm-bin
Patch1: build.patch

%description
IPSEC cryptography library optimized for Intel Architecture

%package dev
Summary: dev components for the intel-ipsec-mb package.
Group: Development
Requires: intel-ipsec-mb-lib = %{version}-%{release}
Provides: intel-ipsec-mb-devel = %{version}-%{release}
Requires: intel-ipsec-mb = %{version}-%{release}

%description dev
dev components for the intel-ipsec-mb package.


%package lib
Summary: lib components for the intel-ipsec-mb package.
Group: Libraries
Requires: intel-ipsec-mb-license = %{version}-%{release}

%description lib
lib components for the intel-ipsec-mb package.


%package license
Summary: license components for the intel-ipsec-mb package.
Group: Default

%description license
license components for the intel-ipsec-mb package.


%prep
%setup -q -n intel-ipsec-mb-1.2
cd %{_builddir}/intel-ipsec-mb-1.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1645635960
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
make  %{?_smp_mflags}  SAFE_DATA=y SAFE_PARAM=y SAFE_LOOKUP=y LIB_INSTALL_DIR=/usr/lib64


%install
export SOURCE_DATE_EPOCH=1645635960
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/intel-ipsec-mb
cp %{_builddir}/intel-ipsec-mb-1.2/LICENSE %{buildroot}/usr/share/package-licenses/intel-ipsec-mb/499ba59c96dc3a1d9bf25928c35248c272799edf
%make_install NOLDCONFIG=y LIB_INSTALL_DIR=/usr/lib64

%files
%defattr(-,root,root,-)
/usr/man/man7/libipsec-mb-dev.7
/usr/man/man7/libipsec-mb.7

%files dev
%defattr(-,root,root,-)
/usr/include/intel-ipsec-mb.h
/usr/lib64/libIPSec_MB.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libIPSec_MB.so.1
/usr/lib64/libIPSec_MB.so.1.2.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/intel-ipsec-mb/499ba59c96dc3a1d9bf25928c35248c272799edf
