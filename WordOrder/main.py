if __name__ == '__main__':
    word_dict = {}
    for _ in range(int(input())):
        current_word = input()
        if word_dict.get(current_word) == None:
            word_dict[current_word] = 1
        else:
            word_dict[current_word] += 1
        
    print(len(word_dict.keys()))
    result_str = ''
    for word_count in word_dict.values():
        result_str += str(word_count) + ' '

    print(result_str)