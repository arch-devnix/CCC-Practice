def function():
    inputs = sys.stdin.read().splitlines()

    if not inputs or len(inputs) < 3:
        return

    B = int(inputs[0]) # Target to buy
    T = int(inputs[1]) # Available
    P = int(inputs[2]) # Already bought

    available = T - P


    if B <= available:
        
        print(f'Y {available - B}')

    else:
        print('N')


# O(1)
