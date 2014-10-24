Feature: Multiplica de dos numeros
	yo como usuario
	quiero multiplica dos numeros
	para obtener un resultado

Scenario: multiplica de 2 por 2
	Given que tengo los numeros 2 por 2
	when realizar la multiplicacion
	then obtengas 4

Scenario: multiplica de 2 por 10
	Given que tengo los numeros 2 por 10
	when realizar la multiplicacion
	then obtengas 20

Scenario: multiplica de 10 por 10
	Given que tengo los numeros 10 por 10
	when realizar la multiplicacion
	then obtengas 100