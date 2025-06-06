#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-File-FcntlLock
Version  : 0.22
Release  : 31
URL      : https://cpan.metacpan.org/authors/id/J/JT/JTT/File-FcntlLock-0.22.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JT/JTT/File-FcntlLock-0.22.tar.gz
Summary  : File locking with L<fcntl(2)>
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-File-FcntlLock-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
Provides: perl-File-FcntlLock-devel = %{version}-%{release}
Requires: perl-File-FcntlLock = %{version}-%{release}

%description dev
dev components for the perl-File-FcntlLock package.


%package perl
Summary: perl components for the perl-File-FcntlLock package.
Group: Default
Requires: perl-File-FcntlLock = %{version}-%{release}

%description perl
perl components for the perl-File-FcntlLock package.


%prep
%setup -q -n File-FcntlLock-0.22
cd %{_builddir}/File-FcntlLock-0.22

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::FcntlLock.3
/usr/share/man/man3/File::FcntlLock::Inline.3
/usr/share/man/man3/File::FcntlLock::Pure.3
/usr/share/man/man3/File::FcntlLock::XS.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
