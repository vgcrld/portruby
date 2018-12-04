%define debug_package %{nil}

%define galileo_base  /opt/galileo
%define galileo_ruby  /opt/galileo/ruby
%define rubyver       2.5.3

Name:           portruby
Version:        1.0
Release:        2
Summary:        A test to build an rpm to instal Ruby
Group:	        dev
License:	      MIT
URL:	          https://galileosuite.com	
Source0:        ruby-%{rubyver}.tar.gz
Source1:        bundler-1.17.1.gem
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
./configure --disable-install-doc --prefix=%{galileo_ruby}
make %{?_smp_mflags}

%install
# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT

# Copy the GEMS to sources
mkdir -p $RPM_BUILD_ROOT/%{galileo_base}/sources
cp ${RPM_SOURCE_DIR}/awesome_print-1.8.0.gem $RPM_BUILD_ROOT/%{galileo_base}/sources/
cp ${RPM_SOURCE_DIR}/bundler-1.17.1.gem      $RPM_BUILD_ROOT/%{galileo_base}/sources/
cp ${RPM_SOURCE_DIR}/optimist-3.0.0.gem      $RPM_BUILD_ROOT/%{galileo_base}/sources/
cp ${RPM_SOURCE_DIR}/sinatra-2.0.4.gem       $RPM_BUILD_ROOT/%{galileo_base}/sources/
cp ${RPM_SOURCE_DIR}/haml-5.0.4.gem          $RPM_BUILD_ROOT/%{galileo_base}/sources/
cp ${RPM_SOURCE_DIR}/nokogiri-1.8.5.gem      $RPM_BUILD_ROOT/%{galileo_base}/sources/
cp ${RPM_SOURCE_DIR}/ruby-oci8-2.2.6.1.gem   $RPM_BUILD_ROOT/%{galileo_base}/sources/

# Install the gems
export PATH=${RPM_BUILD_ROOT}/%{galileo_ruby}/bin:$PATH
gem install --no-document --bindir ${RPM_BUILD_ROOT}/%{galileo_ruby}/bin --install-dir ${RPM_BUILD_ROOT}/%{galileo_ruby}/lib/ruby/gems/2.5.0 ${RPM_BUILD_ROOT}/%{galileo_base}/sources/awesome_print-1.8.0.gem 
gem install --no-document --bindir ${RPM_BUILD_ROOT}/%{galileo_ruby}/bin --install-dir ${RPM_BUILD_ROOT}/%{galileo_ruby}/lib/ruby/gems/2.5.0 ${RPM_BUILD_ROOT}/%{galileo_base}/sources/bundler-1.17.1.gem     
gem install --no-document --bindir ${RPM_BUILD_ROOT}/%{galileo_ruby}/bin --install-dir ${RPM_BUILD_ROOT}/%{galileo_ruby}/lib/ruby/gems/2.5.0 ${RPM_BUILD_ROOT}/%{galileo_base}/sources/optimist-3.0.0.gem    
gem install --no-document --bindir ${RPM_BUILD_ROOT}/%{galileo_ruby}/bin --install-dir ${RPM_BUILD_ROOT}/%{galileo_ruby}/lib/ruby/gems/2.5.0 ${RPM_BUILD_ROOT}/%{galileo_base}/sources/sinatra-2.0.4.gem    
gem install --no-document --bindir ${RPM_BUILD_ROOT}/%{galileo_ruby}/bin --install-dir ${RPM_BUILD_ROOT}/%{galileo_ruby}/lib/ruby/gems/2.5.0 ${RPM_BUILD_ROOT}/%{galileo_base}/sources/haml-5.0.4.gem      
gem install --no-document --bindir ${RPM_BUILD_ROOT}/%{galileo_ruby}/bin --install-dir ${RPM_BUILD_ROOT}/%{galileo_ruby}/lib/ruby/gems/2.5.0 ${RPM_BUILD_ROOT}/%{galileo_base}/sources/nokogiri-1.8.5.gem  
gem install --no-document --bindir ${RPM_BUILD_ROOT}/%{galileo_ruby}/bin --install-dir ${RPM_BUILD_ROOT}/%{galileo_ruby}/lib/ruby/gems/2.5.0 ${RPM_BUILD_ROOT}/%{galileo_base}/sources/ruby-oci8-2.2.6.1.gem 

%files
%defattr(-, root, root, 755 )
%{galileo_base}

%changelog
* Tue Dec 4 2018 Rich Davis <rdavis@galileosuite.com>
- Looks good.
