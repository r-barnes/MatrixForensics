all:
	#./plot_gen.py
	pdflatex --shell-escape matrix_forensics.tex
	bibtex matrix_forensics.aux
	makeindex matrix_forensics.idx
	pdflatex --shell-escape matrix_forensics.tex
	pdflatex --shell-escape matrix_forensics.tex
	cp matrix_forensics.pdf ../

clean:
	rm -f *.bbl *.aux *.run.xml *.bcf *.blg *.out *.fff *.log *.lot *.ttt *.toc *.pyg *.idx *.ind *.ilg *.lof *.spl *-blx.bib *.dvi *.fls *.fdb_latexmk *.listing *.aux.blg