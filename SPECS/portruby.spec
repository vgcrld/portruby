%define galileo_base  /opt/galileo
%define galileo_ruby  /opt/galileo/ruby
%define rubyver       2.2.8

Name:           portruby
Version:        0.1
Release:        1
Summary:        A test to build an rpm to instal Ruby
Group:	        dev
License:	      MIT
URL:	          https://galileosuite.com	
Source0:        ruby-2.2.8.tar.gz
BuildRequires:  readline-devel ncurses-devel gdbm-devel glibc-devel gcc openssl-devel make libyaml-devel libffi-devel zlib-devel
Requires:       readline ncurses gdbm glibc openssl libyaml libffi zlib

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming.  It has many features to process text
files and to do system management tasks (as in Perl).  It is simple,
straight-forward, and extensible.


%prep
%setup -n ruby-%{rubyver}

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"

./configure \
  --enable-shared \
  --disable-rpath \
  --without-X11 \
  --without-tk \
  --disable-install-doc \
  --includedir=%{galileo_ruby}/ruby \
  --libdir=%{galileo_ruby}  \
  --prefix=%{galileo_ruby} \
  --exec_prefix=%{galileo_ruby}

make %{?_smp_mflags}

%install
# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT

# We don't want to keep the src directory
#rm -rf $RPM_BUILD_ROOT%{galileo_ruby}src

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{galileo_base}/*

%changelog

* Thu Nov 22 2018 Rich Davis <rdavis@galileosuite.com>
- Trying to figure this out
