def is_palindrome(text):
    cleaned_text = ''.join([c for c in text if c.isalnum()]).lower()
    print("""Cleaned text: {}""".format(cleaned_text))
    return cleaned_text == cleaned_text[::-1]

print(is_palindrome("A man, a plan, a canal, Panama"))