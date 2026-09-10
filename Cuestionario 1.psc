Algoritmo  OperacionesDirectas
	Definir num1, num2 Como Real
	
	Escribir "Ingrese el primer número:"
	Leer num1
	
	Escribir "Ingrese el segundo número:"
	Leer num2
	
	Escribir "Suma: ", num1 + num2
	Escribir "Resta: ", num1 - num2
	Escribir "Multiplicación: ", num1 * num2
	
	Si num2 = 0 Entonces
		Escribir "No es posible dividir ni calcular el módulo por cero."
	Sino
		Escribir "División: ", num1 / num2
		Escribir "Módulo o residuo: ", num1 mod num2
	FinSi
	
FinAlgoritmo
