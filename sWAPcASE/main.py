def swap_case(s):
    string_clone = ''
    for char in s:
        if char.isupper():
            string_clone += char.lower()
        elif char.islower():
            string_clone += char.upper()
        else:
            string_clone += char
    
    return string_clone

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)