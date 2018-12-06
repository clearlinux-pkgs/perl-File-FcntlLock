#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-FcntlLock
Version  : 0.22
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/J/JT/JTT/File-FcntlLock-0.22.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JT/JTT/File-FcntlLock-0.22.tar.gz
Summary  : File locking with L<fcntl(2)>
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-File-FcntlLock-lib = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
File::FcntlLock
===============
File::FcntlLock is a module to do file locking in an object oriented
fashion using the fcntl(2) system call. This allows locks on parts of
a file as well as on the whole file and overcomes some known problems
with flock(2), on which Perls flock() function is based per default.

%package dev
Summary: dev components for the perl-File-FcntlLock package.
Group: Development
Requires: perl-File-FcntlLock-lib = %{version}-%{release}
Provides: perl-File-FcntlLock-devel = %{version}-%{release}

%description dev
dev components for the perl-File-FcntlLock package.


%package lib
Summary: lib components for the perl-File-FcntlLock package.
Group: Libraries

%description lib
lib components for the perl-File-FcntlLock package.


%prep
%setup -q -n File-FcntlLock-0.22

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/File/FcntlLock.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/File/FcntlLock.pod
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/File/FcntlLock/Core.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/File/FcntlLock/Errors.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/File/FcntlLock/Inline.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/File/FcntlLock/Inline.pod
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/File/FcntlLock/Pure.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/File/FcntlLock/Pure.pod
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/File/FcntlLock/XS.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/File/FcntlLock/XS.pod

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::FcntlLock.3
/usr/share/man/man3/File::FcntlLock::Inline.3
/usr/share/man/man3/File::FcntlLock::Pure.3
/usr/share/man/man3/File::FcntlLock::XS.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/auto/File/FcntlLock/FcntlLock.so
