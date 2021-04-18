Contributors Guide
======================================

Files
--------------------------------------

This subdirectory contains several files. Most are self-explanatory and correspond to sections of the book. A few we describe here:

* [z_math_commands.tex](z_math_commands.tex) - All of the math commands used
* [plot_gen.py](plot_gen.py) - Used to build the plots and diagrams in the book
* [Makefile](Makefile) - Used to build the book
* [refs.bib](refs.bib) - Bibliography



Contributing Equations
--------------------------------------

Note that `z_math_commands.tex` contains extensive simplifying commands for writing equations.

In general equations should be typeset as follows:
```
\begin{equation}
\label{equ:equ_name} %Optional
\eqcite{Thome2016}
\mA = \mB * \mC
\end{equation}
```
Note that `\eqcite{Thome2016}` typesets a citation to `Thome2016` which is an entry in [refs.bib](refs.bib)

Multiple aligned equations can be typeset as follows. Note the careful alignment within the TeX source to improve readability.
```
\begin{align}
\label{equ:equ_name} %Optional
\mA       &= \mB * \mC        \eqcite{Thome2016} \label{equ:a}  \\
\mA + \mB &= \mB + \mC + \mD  \eqcite{Adam2013}  \label{equ:b}  \\
\mA + \mB &= \mB * \mC + \mE  \eqcite{Jane2020}  \label{equ:c}  \\
\end{align}
```
