%global tl_name scale
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.2
Release:	%{tl_revision}.1
Summary:	Scale document by sqrt(2) or magstep(2)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/scale
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scale.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scale.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scale.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package to scale a document by sqrt(2) (or by \magstep{2}). This is
useful if you are preparing a document on, for example, A5 paper and
want to print on A4 paper to achieve a better resolution.

