n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    commands = input().split()
    match commands[0]:
        case 'pop':
            s.pop()
        case 'remove':
            s.remove(int(commands[1]))
        case 'discard':
            s.discard(int(commands[1]))
    
print(sum(s))