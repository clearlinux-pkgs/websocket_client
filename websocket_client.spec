#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : websocket_client
Version  : 1.0.1
Release  : 71
URL      : https://files.pythonhosted.org/packages/2f/34/d513d60a491abe0da2e8b37e28e945957f23f9bf642007f008039788ff2a/websocket-client-1.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/2f/34/d513d60a491abe0da2e8b37e28e945957f23f9bf642007f008039788ff2a/websocket-client-1.0.1.tar.gz
Summary  : WebSocket client for Python with low level API options
Group    : Development/Tools
License  : LGPL-2.1
Requires: websocket_client-bin = %{version}-%{release}
Requires: websocket_client-license = %{version}-%{release}
Requires: websocket_client-python = %{version}-%{release}
Requires: websocket_client-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
[![docs](https://readthedocs.org/projects/websocket-client/badge/?style=flat)](https://websocket-client.readthedocs.io/)
[![Build Status](https://github.com/websocket-client/websocket-client/actions/workflows/build.yml/badge.svg)](https://github.com/websocket-client/websocket-client/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/websocket-client/websocket-client/branch/master/graph/badge.svg?token=pcXhUQwiL3)](https://codecov.io/gh/websocket-client/websocket-client)
[![PyPI Downloads](https://pepy.tech/badge/websocket-client)](https://pepy.tech/project/websocket-client)
[![PyPI version](https://img.shields.io/pypi/v/websocket_client)](https://pypi.org/project/websocket_client/)

%package bin
Summary: bin components for the websocket_client package.
Group: Binaries
Requires: websocket_client-license = %{version}-%{release}

%description bin
bin components for the websocket_client package.


%package license
Summary: license components for the websocket_client package.
Group: Default

%description license
license components for the websocket_client package.


%package python
Summary: python components for the websocket_client package.
Group: Default
Requires: websocket_client-python3 = %{version}-%{release}

%description python
python components for the websocket_client package.


%package python3
Summary: python3 components for the websocket_client package.
Group: Default
Requires: python3-core
Provides: pypi(websocket_client)

%description python3
python3 components for the websocket_client package.


%prep
%setup -q -n websocket-client-1.0.1
cd %{_builddir}/websocket-client-1.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622651454
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/websocket_client
cp %{_builddir}/websocket-client-1.0.1/COPYING.LESSER %{buildroot}/usr/share/package-licenses/websocket_client/5dea8b07199dbcc7be918770ca7cef346f523214
cp %{_builddir}/websocket-client-1.0.1/LICENSE %{buildroot}/usr/share/package-licenses/websocket_client/5dea8b07199dbcc7be918770ca7cef346f523214
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wsdump.py

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/websocket_client/5dea8b07199dbcc7be918770ca7cef346f523214

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
