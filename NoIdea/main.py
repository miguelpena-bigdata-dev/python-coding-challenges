def calculate_happiness(array, setA, setB):
    happiness_score = 0
    
    for integer in array:
        if integer in setA:
            happiness_score += 1
        if integer in setB:
            happiness_score -= 1


    return happiness_score

if __name__ == "__main__":
    n, m = map(int, input().split())
    int_array = list(map(int, input().split()))
    setA = set(map(int, input().split()))
    setB = set(map(int, input().split()))

    happiness_score = calculate_happiness(int_array, setA, setB)
    print(happiness_score)