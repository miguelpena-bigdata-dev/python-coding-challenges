from itertools import groupby

if __name__== '__main__':
    S = input()
    result = []
    for character, group in groupby(S):
        count = len(list(group))
        result.append(f"({count}, {character}) ")
    
    result_text = ''.join(result)
    print(result_text)