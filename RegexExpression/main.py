import re

def replace_operator(matchobj):
    if matchobj.group(0) == ' && ':
        return ' and '
    else:
        return ' or '
    
if __name__ == '__main__':
    pattern = r'\s(\&|\|){2}\s'
    for _ in range(int(input())):
        current_line = input()
        result = re.sub(pattern, replace_operator, current_line)
        print(result)