from random import random
from behave import *
from Pages import calculatorpage
from Pages.calculatorpage import CalculatorPage


@given(u'I launch calculator app')
def step_impl(context):
    context.calculatorpage = CalculatorPage(context.driver)

@when(u'I perform random arithmetic operations')
def step_impl(context):
    num1=random.randint(0,9)
    num2=random.randint(0,9)
    operator=random.choice(['+', '-', '*', '/'])

    context.calculatorpage.tap_digit(str(num1))
    context.calculatorpage.tap_operator(operator)
    context.calculatorpage.tap_digit(str(num2))
    if operator == '+':
        expected_result=str(num1+num2)
    elif operator == '-':
        expected_result=str(num1-num2)
    elif operator == '*':
        expected_result=str(num1*num2)
    elif operator == '/':
        if num2 !=0:
            expected_result = str(num1 / num2)
        else:
            expected_result = "Error"
    context.expected_result=expected_result

@then(u'The result should return accordingly')
def step_impl(context):
    context.calculatorpage.result()


