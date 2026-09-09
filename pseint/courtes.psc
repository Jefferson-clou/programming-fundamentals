Algoritmo courtes 
	//Get data
	//Identiffy process finally
	//1st. level (Grade 1) :30%
	//2nd. level (Grade 2) :30%
	//3th. level (Grade 3) :40%
	//Step 1: Definir variable
	Definir nombre como texto 
	Definir nota1, nota2, nota3, notaFinal Como Real
	//Step 2: Read student name and grades 
	Escribir "enter student name:"
	Leer name
	Escribir "enter first garde (30%):"
	Leer nota1
	Escribir "enter first garde (30%):"
	Leer nota2
	Escribir "enter first garde (40%):"
	Leer nota3
	//Step 3: Process (Calculate weighted avarege)
	notaFinal<- (nota1 *0.30)+(nota2 *0.30)+(nota3 *0.40)
	//Step 4: Ouput result
	Escribir "student", name, "has a final grade of:",notaFinal
FinAlgoritmo
