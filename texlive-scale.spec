Name:		texlive-scale
Version:	15878
Release:	2
Summary:	Scale document by sqrt(2) or magstep(2)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/scale
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scale.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scale.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scale.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package to scale a document by sqrt(2) (or by \magstep{2}).
This is useful if you are preparing a document on, for example,
A5 paper and want to print on A4 paper to achieve a better
resolution.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/scale/scale.sty
%doc %{_texmfdistdir}/doc/latex/scale/COPYING
%doc %{_texmfdistdir}/doc/latex/scale/README
#- source
%doc %{_texmfdistdir}/source/latex/scale/scale.dtx
%doc %{_texmfdistdir}/source/latex/scale/scale.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
