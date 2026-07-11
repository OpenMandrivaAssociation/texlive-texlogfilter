%global tl_name texlogfilter
%global tl_revision 71525

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	Filter LaTeX engines output or log file
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/texlogfilter
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texlogfilter.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texlogfilter.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(texlogfilter.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
texlogfilter is a Perl script designed to filter LaTeX engines output or
log file (LaTeX, pdfLaTeX, LuaLaTeX or XeLaTeX). It reduces the LaTeX
output or log to keep only warnings and errors. The result is colorised.
Options allow to mask specific warnings, such as box or
references/citations warnings. It's also possible to add custom filter
patterns.

