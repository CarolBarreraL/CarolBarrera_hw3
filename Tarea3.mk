Resultados_hw3.pdf: Resultados_hw3.tex Onda30.pdf Onda60.pdf sistemaSolar.pdf
	pdflatex $<

Onda30.pdf: Onda.py
	python Onda.py

Onda60.pdf: Onda.py
	python Onda.py

sistemaSolar.pdf: Plots_Planetas.py
	python Plots_Planetas.py

datos.csv: Planetas.c
	cc Planetas.c -lm -o Planetas.x
	./Planetas.x> datos.csv


	



