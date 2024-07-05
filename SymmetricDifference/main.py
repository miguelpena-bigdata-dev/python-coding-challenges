if __name__ == "__main__":
    M = int(input()) 
    setM = set(map(int, input().split()))
    N = int(input()) 
    setN = set(map(int, input().split()))  

    symmetric_difference_m = list(setM.difference(setN))
    symmetric_difference_n = list(setN.difference(setM))
    result = sorted(symmetric_difference_m + symmetric_difference_n)

    for integer in result:
        print(integer)
