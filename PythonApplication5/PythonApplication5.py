
print("Возняк Софія ІС-01, варіант 24")
print("Першi 10 п'ятизначних палiндромiв")
print("")
counter = 0
number = 100

while (number < 999) & (counter < 10):
    isPrime = True
    number1 = number // 100
    number2 = (number - number1 * 100) // 10
    pol = number * 100 + number2 * 10 + number1

    for i in range(2, pol//2, 1):
        if pol % i == 0:
            isPrime = False
    if isPrime:
        counter = counter + 1
        print(pol)
    if counter < 10 :
        number = number + 1

