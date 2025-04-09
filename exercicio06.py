di = 0
fi = 0
for num in range(5):
    num = int(input(f"digite um numero: "))
    if 10 <= num <=20:
        di = di + 1
    else:
        fi = fi+1

print(f"a quantidade de numeros dentro do intervalo é {di}")
print(f"a quantidade de numeros dentro do intervalo é {fi}")