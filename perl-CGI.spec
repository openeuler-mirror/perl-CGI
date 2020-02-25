%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((File::Spec|File::Temp|MultipartBuffer|Fh)\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Fh\\)


Name:           perl-CGI
Summary:        Handle Common Gateway Interface requests and responses
Version:        4.46
Release:        1
License:        (GPL+ or Artistic) and Artistic 2.0
URL:            https://metacpan.org/release/CGI
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEEJO/CGI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils findutils glibc-common make
BuildRequires:  perl-generators perl-interpreter perl(ExtUtils::MakeMaker)
# Run-requires:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp) perl(Exporter) perl(parent) perl(strict)
BuildRequires:  perl(File::Spec) perl(File::Temp) perl(HTML::Entities)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | cut -d"'" -f 2))
Requires:       perl(File::Spec) perl(File::Temp) perl(HTML::Entities) perl(Text::ParseWords)

%{?perl_default_filter}

%description
CGI.pm is a stable, complete and mature solution for processing and preparing
HTTP requests and responses. Major features including processing form submissions,
file uploads, reading and writing cookies, query string generation and manipulation,
and processing and preparing HTTP headers.

CGI.pm performs very well in in a vanilla CGI.pm environment and also comes with
built-in support for mod_perl and mod_perl2 as well as FastCGI.

%package_help

%prep
%autosetup -n CGI-%{version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
# test need perl(Test::Warn) module
#make test

%files
%license LICENSE
%doc README.md examples/
%{perl_vendorlib}/*

%files help
%doc Changes README.md
%{_mandir}/man3/*.3*

%changelog
* Tue Feb 25 2020 openEuler Buildteam <buildteam@openeuler.org> - 4.46-1
- Package init
