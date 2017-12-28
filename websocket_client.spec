#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : websocket_client
Version  : 0.45.0
Release  : 26
URL      : http://pypi.debian.net/websocket_client/websocket_client-0.45.0.tar.gz
Source0  : http://pypi.debian.net/websocket_client/websocket_client-0.45.0.tar.gz
Summary  : WebSocket client for python. hybi13 is supported.
Group    : Development/Tools
License  : LGPL-2.1
Requires: websocket_client-bin
Requires: websocket_client-python3
Requires: websocket_client-python
Requires: six
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six

%description
websocket-client
        =================

%package bin
Summary: bin components for the websocket_client package.
Group: Binaries

%description bin
bin components for the websocket_client package.


%package python
Summary: python components for the websocket_client package.
Group: Default
Requires: websocket_client-python3

%description python
python components for the websocket_client package.


%package python3
Summary: python3 components for the websocket_client package.
Group: Default
Requires: python3-core

%description python3
python3 components for the websocket_client package.


%prep
%setup -q -n websocket_client-0.45.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1514477012
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wsdump.py

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
