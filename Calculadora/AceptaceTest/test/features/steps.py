# -*- coding: utf-8 -*-
from lettuce import *
import sys
sys.path.append("../")
from calculadora import calculadora


@step(u'Given que tengo los numeros (\d+) mas (\d+)')
def given_que_tengo_los_numeros_2_mas_dos(step, numero1, numero2):
    world.numero1 = int(numero1)
    world.numero2 = int(numero2)


@step(u'when realizó la suma')
def when_realizo_la_suma(step):
    cal=calculadora()
    world.resultado = cal.suma(world.numero1, world.numero2)


@step(u'then obtengo (\d+)')
def then_obtengo_4(step, total):
    assert world.resultado == int(total), 'resultado {0} esperado {1}'.format(
        world.resultado, int(total))


@step(u'Given que tengo los numeros (\d+) menos (\d+)')
def given_que_tengo_los_numeros_2_menos_2(step, num1, num2):
    world.num1 = int(num1)
    world.num2 = int(num2)


@step(u'when realizar la resta')
def when_realizar_la_resta(step):
    cal=calculadora()
    world.resultado1 = cal.resta(world.num1, world.num2)


@step(u'then obtener (\d+)')
def then_obtener_0(step, total1):
    assert world.resultado1 == int(total1), 'resultado {0} esperado {1}'.format(
        world.resultado1, int(total1))


@step(u'Given que tengo los numeros (\d+) por (\d+)')
def given_que_tengo_los_numeros_2_por_2(step, n1, n2):
    world.n1 = int(n1)
    world.n2 = int(n2)


@step(u'when realizar la multiplicacion')
def when_realizar_la_multiplicacion(step):
    cal=calculadora()
    world.resultado2 = cal.multiplicacion(world.n1, world.n2)


@step(u'then obtengas (\d+)')
def then_obtengas_4(step, t2):
    assert world.resultado2 == int(t2), 'resultado {0} esperado {1}'.format(
        world.resultado2, int(t2))


@step(u'Given que tengo los numeros (\d+) entre (\d+)')
def given_que_tengo_los_numeros_2_entre_2(step, nu1, nu2):
    world.nu1 = int(nu1)
    world.nu2 = int(nu2)


@step(u'when realizar la division')
def when_realizar_la_division(step):
    cal=calculadora()
    world.resultado3 = cal.division(world.nu2, world.nu1)


@step(u'then obtenga (\d+)')
def then_obtenga_1(step, t3):
    assert world.resultado3 == int(t3), 'resultado {0} esperado {1}'.format(
        world.resultado3, int(t3))



