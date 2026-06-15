def is_palindrome_simple(text):
    cleaned_text = text.lower()
    return cleaned_text == cleaned_text[::-1]
b=input("Enter the word : ")
if is_palindrome_simple(b):
    print(f"'{b}' is a palindrome!")
else:
    print(f"'{b}' is not a palindrome.")
