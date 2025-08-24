txt1=input("Enter the word")
def sen(txt1):
    if txt1==txt1[::-1]:
        return "palindrome"
    else:
        return "not palindrome"
s=sen(txt1)
print(s)

