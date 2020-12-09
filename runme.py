from fizzbuzz import fizzbuzz
import os

os.system("clear")
print("\n========== FizzBuzz ==========\n\n1. Run Fizzbuzz\n2. Exit")
option = input("\nChoose an option: ").strip()

if option == "1":
    fizzbuzzupto = int(input("\nPlease input a number to count up to: ").strip())
    fizzbuzznum1 = int(input("Please input the fizz number: ").strip())
    fizzbuzznum2 = int(input("Please input the buzz number: ").strip())
    print("")
    fizzbuzz(fizzbuzznum1, fizzbuzznum2, fizzbuzzupto)
    input("\n========== Press enter to close ==========")
    os.system("clear")
elif option == "2":
    os.system("clear")
    exit()
else:
    print("Please choose an option, 1 or 2")