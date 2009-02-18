%define name dparser
%define version 1.15
%define release %mkrel 1

Summary: Simple but powerful tool for parsing
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://aleron.dl.sourceforge.net/sourceforge/dparser/d-%{version}-src.tar.bz2
Source1: python-dparser-calc.tar.bz2
Patch1: dparser-makefile.patch.bz2
License: BSD
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
Url: http://dparser.sourceforge.net/
BuildRequires: libpython-devel
BuildRequires: python

%description
DParser is an simple but powerful tool for parsing. You can specify the form of
the text to be parsed using a combination of regular expressions and grammar
productions.  Because of the parsing technique (technically a scannerless GLR
parser based on the Tomita algorithm) there are no restrictions.   The grammar
can be ambiguous, right or left recursive, have any number of null productions,
and because there is no separate tokenizer, can include whitespace in terminals
and have terminals which are prefixes of other terminals.   DParser handles not
just well formed computer languages and data files, but just about any wacky
situation that occurs in the real world.


%package -n python-%{name}

Summary: DParser python binding
Requires: python
Group: Development/Python

%description  -n python-%{name}
DParser is a simple but powerful tool for parsing, written by J. Plevyak.
DParser for Python gives Python programmers a seamless interface to DParser.

The features that set this Python parser apart from other Python parsers are:
 + it can deal with any grammar (GLR)
 + it is fast (based in C)
 + it does not require a compiler to operate.

DParser for Python also has many easy-to-use features found in other Python
parsers:
 + it does not require explicit definitions of tokens
 + it does not require a separate, non-Python grammar file
 + it uses function documentation strings to specify grammar rules
 + it does not output parser code that the user must compile or run.

%prep

%setup -q -n d
%setup -q -T -D -a 1 -n d

#%patch1 -p1

%build
make
#make test

%install
rm -rf $RPM_BUILD_ROOT
PREFIX=$RPM_BUILD_ROOT%_prefix make install
cd python
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

mkdir -p $RPM_BUILD_ROOT%_mandir/man1
mv  $RPM_BUILD_ROOT%_prefix/man/man1/* $RPM_BUILD_ROOT%_mandir/man1/
%ifarch x86_64
mv  $RPM_BUILD_ROOT{/usr/lib,%_libdir}/libdparse.a
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%_bindir/*
%_includedir/*
%_libdir/*.a
%_libdir/python%pyver/site-packages/*
%_mandir/man1/*
%defattr(644,root,root,755)
%doc BUILD_VERSION CHANGES COPYRIGHT README *.html tests verilog

%files  -n python-%{name} -f python/INSTALLED_FILES
%defattr(-,root,root,0755)
%doc python/README python/*.html python/tests python/contrib python/calc.py

