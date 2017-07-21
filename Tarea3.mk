Resultados_hw3.pdf: Resultados_hw3.tex Onda30.pdf Onda60.pdf sistemaSolar.pdf
	pdflatex $<

sistemaSolar.pdf: Planetas.c Plots_Planetas.py
	cc Planetas.c -lm -o Planetas.x
	./Planetas.x> datos.csv
	python Plots_Planetas.py

Onda30.pdf: Onda.py
	python Onda.py

Onda60.pdf: Onda.py
	python Onda.py



	



