from itertools import groupby

if __name__== '__main__':
    S = input()
    result = []
    for _, group in groupby(S):
        group_list = list(group)
        result.append((len(group_list), int(group_list[0])))
    result_text = ''
    for item in result:
        result_text += str(item) + ' '

    print(result_text)