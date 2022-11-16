Name:		texlive-texlogfilter
Version:	62792
Release:	1
Summary:	Filter LaTeX engines output or log file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/texlogfilter
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlogfilter.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlogfilter.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
texlogfilter is a Perl script designed to filter LaTeX engines
output or log file (LaTeX, pdfLaTeX, LuaLaTeX or XeLaTeX). It
reduces the LaTeX output or log to keep only warnings and
errors. The result is colorised. Options allow to mask specific
warnings, such as box or references/citations warnings. It's
also possible to add custom filter patterns.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/scripts/texlogfilter
%doc %{_texmfdistdir}/texmf-dist/doc/support/texlogfilter
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/texlogfilter.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/texlogfilter.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
