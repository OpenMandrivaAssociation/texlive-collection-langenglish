Name:		texlive-collection-langenglish
Epoch:		1
Version:	63184
Release:	2
Summary:	US and UK English
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langenglish.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-hyphen-english
Requires:	texlive-FAQ-en
Requires:	texlive-MemoirChapStyles
Requires:	texlive-Type1fonts
Requires:	texlive-amslatex-primer
Requires:	texlive-around-the-bend
Requires:	texlive-ascii-chart
Requires:	texlive-components-of-TeX
Requires:	texlive-comprehensive
Requires:	texlive-dickimaw
Requires:	texlive-dtxtut
Requires:	texlive-first-latex-doc
Requires:	texlive-gentle
Requires:	texlive-guide-to-latex
Requires:	texlive-happy4th
Requires:	texlive-impatient
Requires:	texlive-intro-scientific
Requires:	texlive-knuth
Requires:	texlive-l2tabu-english
Requires:	texlive-latex-brochure
Requires:	texlive-latex-course
Requires:	texlive-latex-doc-ptr
Requires:	texlive-latex-graphics-companion
Requires:	texlive-latex-veryshortguide
Requires:	texlive-latex-web-companion
Requires:	texlive-latex2e-help-texinfo
Requires:	texlive-latex4wp
Requires:	texlive-latexcheat
Requires:	texlive-latexfileinfo-pkgs
Requires:	texlive-lshort-english
Requires:	texlive-macros2e
Requires:	texlive-math-e
Requires:	texlive-memdesign
Requires:	texlive-metafont-beginners
Requires:	texlive-metapost-examples
Requires:	texlive-mil3
Requires:	texlive-patgen2-tutorial
Requires:	texlive-pictexsum
Requires:	texlive-plain-doc
Requires:	texlive-presentations-en
Requires:	texlive-pstricks-examples-en
Requires:	texlive-simplified-latex
Requires:	texlive-svg-inkscape
Requires:	texlive-tabulars-e
Requires:	texlive-tamethebeast
Requires:	texlive-tds
Requires:	texlive-tex-font-errors-cheatsheet
Requires:	texlive-tex-overview
Requires:	texlive-tex-refs
Requires:	texlive-texbytopic
Requires:	texlive-titlepages
Requires:	texlive-tlc2
Requires:	texlive-visualfaq
Requires:	texlive-voss-mathmode
Requires:	texlive-webguide
Requires:	texlive-xetexref

%description
Support for (and documentation in) English.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
