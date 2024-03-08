num_um = int(input('Digite um número: '))
num_dois = int(input('Digite outro número: '))

op = input('Digite qual operação matemática você quer usar. Ex.: +, -, /, *: ')

if op == '+':
    print(num_um + num_dois)
elif op == '-':
    print(num_um - num_dois)
elif op == '/':
    print(num_um / num_dois)
elif op == '*':
    print(num_um * num_dois)