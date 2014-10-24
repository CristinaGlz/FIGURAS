Feature: Resta de dos numeros
	yo como usuario
	quiero restar dos numeros
	para obtener un resultado

Scenario: resta de 2 menos 2
	Given que tengo los numeros 2 menos 2
	when realizar la resta 
	then obtener 0

Scenario: resta de 2 menos 1
	Given que tengo los numeros 2 menos 1
	when realizar la resta 
	then obtener 1

Scenario: resta de 10 menos 3
	Given que tengo los numeros 10 menos 3
	when realizar la resta 
	then obtener 7