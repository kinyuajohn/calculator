import math


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def mod(a, b):
    return a % b


def lcm(a, b):
    l = math.lcm(a, b)
    return l


def hcf(a, b):
    h = math.gcd(a, b)
    return h


def find_numbers(text_list):
    numbers_in_text_list = []
    for number in text_list:
        try:
            numbers_in_text_list.append(float(number))
        except ValueError:
            pass
    return numbers_in_text_list


# fmt: off
operations = {
    'ADD':add,'ADDITION':add,'SUM':add,'PLUS':add, '+':add,
    'SUBTRACTION':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub, '-':sub,
    'PRODUCT': mul, 'MULTIPLICATION': mul,'MULTIPLY': mul, 'TIMES': mul, '*': mul,
    'DIVISION': div, 'DIV': div, 'DIVIDE': div, '/': div,
    'LCM':lcm , 'HCF':hcf,
    'MOD':mod ,'REMAINDER':mod , 'MODULUS':mod 
}
# fmt:on

text = "What is 1 + 1"

text_list = text.split(" ")
print(text_list)

for word in text_list:
    if word.upper() in operations.keys():
        number_list = find_numbers(text_list)
        print(number_list)

        # result = operations[word.upper()](number_list[0], number_list[1])
        # print(result)

print(operations["+"](1, 1))
