all:
	#./plot_gen.py
	pdflatex --shell-escape matrix_forensics.tex
	bibtex matrix_forensics.aux
	makeindex matrix_forensics.idx
	pdflatex --shell-escape matrix_forensics.tex
	pdflatex --shell-escape matrix_forensics.tex
