word = str(input("Enter a word to check if it's a palindrome: \n"))
is_palindrome = word.find(word[::-1])
print(word)
print((word[::-1]))
if is_palindrome == 0:
    print("True")
else:
    print(" False")