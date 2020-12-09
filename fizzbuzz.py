def fizzbuzz(num1 , num2, maxnumber):
    for i in range(maxnumber):
        j = i + 1
        if j % num1 == 0 and j % num2 == 0:
            print(f"{str(j)}. fizzbuzz")
        elif j % num1 == 0:
            print(f"{str(j)}. fizz")
        elif j % num2 == 0:
            print(f"{str(j)}. buzz")
        else:
            print(f"{str(j)}. {str(j)}")