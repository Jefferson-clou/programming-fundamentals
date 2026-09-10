Algoritmo DaysToTimeUnits
	// Declaration variable
	Definir days, totalHours, totalMinutes, totalSeconds Como Real
	
	// Get data from user
	Escribir "DAYS CONVERTER "
	Escribir "Enter total number of days:"
	Leer days
	
	// Operations
	// 1 day = 24 hours, 1440 minutes, 86400 seconds
	totalHours <- days * 24
	totalMinutes <- days * 1440
	totalSeconds <- days * 86400
	
	// Output results
	Escribir "Equivalent in hours: ", totalHours
	Escribir "Equivalent in minutes: ", totalMinutes
	Escribir "Equivalent in seconds: ", totalSeconds
FinAlgoritmo