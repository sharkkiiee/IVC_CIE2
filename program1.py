n = int(input("Enter a number: "))
s = sum(int(d) for d in str(n))

if str(s) == str(s) [::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")