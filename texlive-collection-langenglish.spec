%global tl_name collection-langenglish
%global tl_revision 78607

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	US and UK English
Group:		Publishing
URL:		https://www.ctan.org/pkg/collection-langenglish
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langenglish.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(amiweb2c-guide)
Requires:	texlive(amscls-doc)
Requires:	texlive(amslatex-primer)
Requires:	texlive(around-the-bend)
Requires:	texlive(ascii-chart)
Requires:	texlive(asy-overview)
Requires:	texlive(biblatex-cheatsheet)
Requires:	texlive(collection-basic)
Requires:	texlive(components)
Requires:	texlive(comprehensive)
Requires:	texlive(dickimaw)
Requires:	texlive(docsurvey)
Requires:	texlive(drawing-with-metapost)
Requires:	texlive(dtxtut)
Requires:	texlive(first-latex-doc)
Requires:	texlive(fontinstallationguide)
Requires:	texlive(forest-quickstart)
Requires:	texlive(gentle)
Requires:	texlive(guide-to-latex)
Requires:	texlive(happy4th)
Requires:	texlive(hyphen-english)
Requires:	texlive(impatient)
Requires:	texlive(intro-scientific)
Requires:	texlive(knuth-errata)
Requires:	texlive(knuth-hint)
Requires:	texlive(knuth-pdf)
Requires:	texlive(l2tabu-english)
Requires:	texlive(latex-brochure)
Requires:	texlive(latex-course)
Requires:	texlive(latex-doc-ptr)
Requires:	texlive(latex-for-undergraduates)
Requires:	texlive(latex-graphics-companion)
Requires:	texlive(latex-refsheet)
Requires:	texlive(latex-veryshortguide)
Requires:	texlive(latex-web-companion)
Requires:	texlive(latex2e-help-texinfo)
Requires:	texlive(latex4wp)
Requires:	texlive(latexcheat)
Requires:	texlive(latexcourse-rug)
Requires:	texlive(latexfileinfo-pkgs)
Requires:	texlive(lshort-english)
Requires:	texlive(macros2e)
Requires:	texlive(math-into-latex-4)
Requires:	texlive(maths-symbols)
Requires:	texlive(memdesign)
Requires:	texlive(memoirchapterstyles)
Requires:	texlive(metafont-beginners)
Requires:	texlive(metapost-examples)
Requires:	texlive(patgen2-tutorial)
Requires:	texlive(pictexsum)
Requires:	texlive(plain-doc)
Requires:	texlive(quran-en)
Requires:	texlive(short-math-guide)
Requires:	texlive(simplified-latex)
Requires:	texlive(svg-inkscape)
Requires:	texlive(tamethebeast)
Requires:	texlive(tds)
Requires:	texlive(tex-font-errors-cheatsheet)
Requires:	texlive(tex-nutshell)
Requires:	texlive(tex-overview)
Requires:	texlive(tex-vpat)
Requires:	texlive(texbytopic)
Requires:	texlive(texonly)
Requires:	texlive(titlepages)
Requires:	texlive(tlc2)
Requires:	texlive(tlc3-examples)
Requires:	texlive(tlmgrbasics)
Requires:	texlive(typstfun)
Requires:	texlive(undergradmath)
Requires:	texlive(visualfaq)
Requires:	texlive(webguide)
Requires:	texlive(wrapstuff-doc-en)
Requires:	texlive(yet-another-guide-latex2e)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Support for, and documentation in, English.

