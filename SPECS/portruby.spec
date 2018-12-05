%define debug_package %{nil}

%define galileo_base  /opt/galileo
%define galileo_ruby  /opt/galileo/ruby
%define rubyver       2.5.3
%define gemdir        /opt/galileo/ruby/lib/ruby/gems/2.5.0

Name:           portruby
Version:        1.0
Release:        2
Summary:        Ruby Installed to /opt/galileo/ruby
Group:	        dev
License:	      MIT
URL:	          https://galileosuite.com	
Source0:        ruby-%{rubyver}.tar.gz
Source1:        bundler-1.17.1.gem
BuildRequires:  readline-devel ncurses-devel gdbm-devel glibc-devel gcc openssl-devel make libyaml-devel libffi-devel zlib-devel
Requires:       readline ncurses gdbm glibc openssl libyaml libffi zlib

%description
Galileo base ruby

%prep
%setup -n ruby-%{rubyver}

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"
./configure --disable-install-doc --prefix=%{galileo_ruby}
make %{?_smp_mflags}

%install
# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT
 
# Install the gems in SOURCE
export PATH=${RPM_BUILD_ROOT}/%{galileo_ruby}/bin:$PATH
cd ${RPM_SOURCE_DIR}
gem install bundler-1.17.1.gem    --bindir %{_tmppath}/gems/bin --install-dir %{_tmppath}/gems/lib --no-document --local
gem install sinatra-2.0.4.gem     --bindir %{_tmppath}/gems/bin --install-dir %{_tmppath}/gems/lib --no-document --local
gem install nokogiri-1.8.5.gem    --bindir %{_tmppath}/gems/bin --install-dir %{_tmppath}/gems/lib --no-document --local
gem install ruby-oci8-2.2.6.1.gem --bindir %{_tmppath}/gems/bin --install-dir %{_tmppath}/gems/lib --no-document --local

# gem data 
cp    %{_tmppath}/gems/bin/* ${RPM_BUILD_ROOT}/%{galileo_ruby}/bin/
cp -r %{_tmppath}/gems/lib/* ${RPM_BUILD_ROOT}/%{galileo_ruby}/lib/ruby/gems/2.5.0

# Bundle install - copy the 
## bundle install --gemfile ${RPM_SOURCE_DIR}/Gemfile --path %{_tmppath}/gems/lib/
## cp -r %{_tmppath}/gems/lib ${RPM_BUILD_ROOT}/%{galileo_ruby}/lib/ruby/gems/2.5.0/

%files
%defattr(-, root, root, 755 )
%{galileo_base}

%changelog
* Tue Dec 4 2018 Rich Davis <rdavis@galileosuite.com>
- Looks good.
