num = int(input(f"digite um numero: "))
if num <= 0:
    print("numero invalido")
else:
    for num in range(1,num + 1,1):
        print(num, end=" ")