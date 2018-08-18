#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : websocket_client
Version  : 0.50.0
Release  : 43
URL      : https://files.pythonhosted.org/packages/93/b6/254deba82e04b6de6e0e0ac40d251a0f1300724e82e85a68e6565eab7e69/websocket_client-0.50.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/93/b6/254deba82e04b6de6e0e0ac40d251a0f1300724e82e85a68e6565eab7e69/websocket_client-0.50.0.tar.gz
Summary  : WebSocket client for Python. hybi13 is supported.
Group    : Development/Tools
License  : LGPL-2.1
Requires: websocket_client-bin
Requires: websocket_client-python3
Requires: websocket_client-license
Requires: websocket_client-python
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : six

%description
websocket-client
        =================
        
        websocket-client module  is WebSocket client for python. This provide the low level APIs for WebSocket. All APIs are the synchronous functions.
        
        websocket-client supports only hybi-13.
        
        
        License
        ============
        
         - LGPL
        
        Installation
        =============
        
        This module is tested on Python 2.7 and Python 3.4+.
        
        Type "python setup.py install" or "pip install websocket-client" to install.

%package bin
Summary: bin components for the websocket_client package.
Group: Binaries
Requires: websocket_client-license

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
%setup -q -n websocket_client-0.50.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534605999
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/websocket_client
cp LICENSE %{buildroot}/usr/share/doc/websocket_client/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wsdump.py

%files license
%defattr(-,root,root,-)
/usr/share/doc/websocket_client/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
