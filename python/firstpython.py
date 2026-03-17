text = input("Enter a word: ")

# reverse the string
rev = text[::-1]

if text == rev:
    print("Palindrome ✅")
else:
    print("Not a Palindrome ❌")