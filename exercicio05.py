negativo = 0
for num in range(1,5,1):
    num = int(input("digite um numero: "))
    if num < 0:
        negativo = negativo + 1
print(f"existem {negativo} negativos")