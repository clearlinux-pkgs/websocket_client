#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : websocket_client
Version  : 0.37.0
Release  : 14
URL      : https://pypi.python.org/packages/source/w/websocket-client/websocket_client-0.37.0.tar.gz
Source0  : https://pypi.python.org/packages/source/w/websocket-client/websocket_client-0.37.0.tar.gz
Summary  : WebSocket client for python. hybi13 is supported.
Group    : Development/Tools
License  : LGPL-2.1
Requires: websocket_client-bin
Requires: websocket_client-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python

%description
=================
websocket-client
=================
websocket-client module  is WebSocket client for python. This provide the low level APIs for WebSocket. All APIs are the synchronous functions.

%package bin
Summary: bin components for the websocket_client package.
Group: Binaries

%description bin
bin components for the websocket_client package.


%package python
Summary: python components for the websocket_client package.
Group: Default
Requires: six-python

%description python
python components for the websocket_client package.


%prep
%setup -q -n websocket_client-0.37.0

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wsdump.py

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
