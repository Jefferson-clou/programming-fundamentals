Algoritmo AveregeFiveNumbers
	//Declaration variable
	Definir suma, promedio Como Real
	Definir num1, num2, num3, num4, num5 Como Real
	//Ask the user for the five numbers
	Escribir "Enter the first number: "
	Leer num1
	Escribir "Enter the second number: "
	Leer num2
	Escribir "Enter the third number: "
	Leer num3
	Escribir "Enter the fourth number: "
	Leer num4
	Escribir "Enter the fifth number: "
	Leer num5
	//Perform the operations 
	suma <- num1 + num2 + num3 + num4 + num5 
	promedio <- suma / 5
	//Result
	Escribir "La suma de los numeros es: ", suma
	Escribir "El promedio es: ", promedio
FinAlgoritmo
