# Build script for RAPPORT_PFA Tamwil AI
# Uses pdflatex + bibtex (biber/latexmk not required).

MAIN = rapport
TEX  = pdflatex -interaction=nonstopmode -halt-on-error
BIB  = bibtex

.PHONY: all clean cleanall watch

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex preamble.tex titlepage.tex \
             $(wildcard frontmatter/*.tex) \
             $(wildcard chapters/*.tex) \
             $(wildcard annexes/*.tex) \
             $(wildcard figures/*.tex) \
             references.bib
	$(TEX) $(MAIN).tex
	-$(BIB) $(MAIN)
	$(TEX) $(MAIN).tex
	$(TEX) $(MAIN).tex

clean:
	rm -f *.aux *.log *.toc *.lof *.lot *.out *.bbl *.blg *.bcf *.run.xml *.synctex.gz
	rm -f chapters/*.aux frontmatter/*.aux annexes/*.aux figures/*.aux

cleanall: clean
	rm -f $(MAIN).pdf

watch:
	while inotifywait -e modify $(MAIN).tex chapters/*.tex frontmatter/*.tex annexes/*.tex figures/*.tex preamble.tex; do \
	    make; \
	done
