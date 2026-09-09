Algoritmo student_grades
	Definir n1, n2, n3, def Como Real
	Definir fullname Como Caracter
	n1<-0
	n2<-0
	n3<-0
	def<-0
	fulname<- ""
	Escribir "Type fullname: "
	Leer fullname
	Escribir "type n1:"
	Leer n1
	Escribir "type n2:"
	Leer n2
	Escribir "type n3:"
	Leer n3
	def<-n1*0.3 + n2 *0.3 + n3*0.4
	Escribir "hola" + fullname + ", final grade is: ", def
	Escribir "grades averages is: ", (n1+n2+n3)/3
FinAlgoritmo
