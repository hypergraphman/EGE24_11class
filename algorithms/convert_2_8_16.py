n = 9
print(bin(n)[2:].rjust(8, '0'))
print(oct(n)[2:].rjust(3, '0'))
print(hex(n)[2:].rjust(2, '0'))
print()
print(f'{n:0>8b}')
print(f'{n:0>3o}')
print(f'{n:0>2x}')
print('----------')
print(int('1234', 5))