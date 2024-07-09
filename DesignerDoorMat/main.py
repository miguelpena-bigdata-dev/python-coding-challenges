if __name__ == '__main__':
    n, m = map(int, input().split())
    design_one, design_two = '.|.', 'WELCOME'
    top_half = [(design_one*i).center(m, '-') for i in range(1, (n // 2) * 2, 2)]
    center_txt = design_two.center(m, '-')
    bottom_half = [(design_one*i).center(m, '-') for i in reversed(range(1, (n // 2) * 2, 2))]

    print('\n'.join(top_half))
    print(center_txt)
    print('\n'.join(bottom_half))