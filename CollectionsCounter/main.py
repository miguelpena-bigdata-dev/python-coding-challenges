from collections import Counter

def main():
    shoes: int = int(input())
    shoe_count = Counter(map(lambda item: int(item), input().split(' ')))
    desired_shoes = [tuple(map(lambda x: int(x), input().split(' '))) for _ in range(int(input()))]
    total = 0
    for desired_shoe in desired_shoes:
        remaining = shoe_count.get(desired_shoe[0])
        if remaining != None and remaining > 0:
            shoe_count.subtract({desired_shoe[0], 1})
            total += desired_shoe[1]

    print(total)


if __name__ == '__main__':
    main()