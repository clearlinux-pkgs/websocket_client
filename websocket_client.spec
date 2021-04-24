#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : websocket_client
Version  : 0.58.0
Release  : 70
URL      : https://files.pythonhosted.org/packages/4a/df/112c278ba1ead96786d24d973429ce1e1a2c86b9843183d9f8ef8c6330d7/websocket_client-0.58.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/4a/df/112c278ba1ead96786d24d973429ce1e1a2c86b9843183d9f8ef8c6330d7/websocket_client-0.58.0.tar.gz
Summary  : WebSocket client for Python with low level API options
Group    : Development/Tools
License  : LGPL-2.1
Requires: websocket_client-bin = %{version}-%{release}
Requires: websocket_client-license = %{version}-%{release}
Requires: websocket_client-python = %{version}-%{release}
Requires: websocket_client-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : six

%description
=================
websocket-client
=================
websocket-client module  is WebSocket client for python. This provide the low level APIs for WebSocket. All APIs are the synchronous functions.

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
Requires: pypi(six)

%description python3
python3 components for the websocket_client package.


%prep
%setup -q -n websocket_client-0.58.0
cd %{_builddir}/websocket_client-0.58.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1614788651
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
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/websocket_client
cp %{_builddir}/websocket_client-0.58.0/LICENSE %{buildroot}/usr/share/package-licenses/websocket_client/5dea8b07199dbcc7be918770ca7cef346f523214
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
