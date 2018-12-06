%define debug_package %{nil}

%define galileo_base  /opt/galileo
%define galileo_ruby  /opt/galileo/ruby
%define galileo_src   /opt/galileo/sources
%define bundle_gem    bundler-1.17.1.gem
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

# Bundle to tmp and copy to avoid rpm fail on path check
mkdir -p %{_tmppath}/bundle
cp ${RPM_SOURCE_DIR}/Gemfile %{_tmppath}/bundle/Gemfile
rbenv global %{rubyver}
bundle install --gemfile %{_tmppath}/bundle/Gemfile --path %{_tmppath}/bundle/vendor

%install
make install DESTDIR=$RPM_BUILD_ROOT

# Include bundler source gem and copy bundle created above
mkdir -p ${RPM_BUILD_ROOT}/%{galileo_ruby}
mkdir -p ${RPM_BUILD_ROOT}/%{galileo_src}
cp -r ${RPM_SOURCE_DIR}/%{bundle_gem} ${RPM_BUILD_ROOT}/%{galileo_src}/%{bundle_gem}
cp -r %{_tmppath}/bundle/* ${RPM_BUILD_ROOT}/%{galileo_ruby}

%post
export PATH=%{galileo_ruby}/bin:$PATH
gem install %{galileo_src}/%{bundle_gem}

%files
%defattr(-, root, root, 755 )
%{galileo_base}

#%clean 
#rm -rf %{_tmppath}/bundle

%changelog
* Tue Dec 4 2018 Rich Davis <rdavis@galileosuite.com>
- Looks good.
