def count_substring(string, sub_string):
    sub_string_length = len(sub_string)
    if sub_string_length > len(string):
        return 0
    
    count_value = 0
    for start_value in range(0, len(string)):
        current_substring = string[start_value:start_value + sub_string_length]
        if current_substring == sub_string:
            count_value += 1

    return count_value

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)