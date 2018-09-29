from funcs import findPI;
import math

n = input('Введите число итераций: ')
try:
    n = int(n)
except ValueError:
    print('Ожидается целое число')

print(findPI(n))