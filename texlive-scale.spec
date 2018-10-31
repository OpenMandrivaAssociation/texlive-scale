# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/scale
# catalog-date 2006-11-06 12:20:58 +0100
# catalog-license gpl
# catalog-version 1.1.2
Name:		texlive-scale
Version:	1.1.2
Release:	11
Summary:	Scale document by sqrt(2) or magstep(2)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/scale
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scale.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scale.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scale.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1.2-2
+ Revision: 755796
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1.2-1
+ Revision: 719487
- texlive-scale
- texlive-scale
- texlive-scale
- texlive-scale

