num_um = int(input('Digite um número: '))
num_dois = int(input('Digite outro número: '))
num_tres = int(input('Digite mais outro número: '))

if num_um > num_dois and num_tres:
    print(f'{num_um} é o maior')
elif num_dois > num_um and num_tres:
    print(f'{num_dois} é o maior')
else:
    print(f'{num_tres} é o maior')