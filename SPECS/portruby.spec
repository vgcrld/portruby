%define debug_package %{nil}

%define galileo_base  /opt/galileo
%define galileo_ruby  /opt/galileo/ruby
%define rubyver       2.5.3

Name:           portruby
Version:        1.0
Release:        2
Summary:        Galileo Ruby Base Install
Group:	        dev
License:	      MIT
URL:	          https://galileosuite.com	
Source0:        ruby-%{rubyver}.tar.gz
BuildRequires:  readline-devel ncurses-devel gdbm-devel glibc-devel gcc openssl-devel make libyaml-devel libffi-devel zlib-devel
Requires:       readline ncurses gdbm glibc openssl libyaml libffi zlib

%description
Fully functioning Ruby installed to /opt/galileo/ruby

%prep
%setup -n ruby-%{rubyver}

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"
./configure --disable-install-doc --prefix=%{galileo_ruby}
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-, root, root, 755 )
%{galileo_base}

%changelog
* Tue Dec 4 2018 Rich Davis <rdavis@galileosuite.com>
- Looks good.
