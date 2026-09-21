import sys

def function():
    inputs = sys.stdin.read().split()
    if len(inputs) < 2:
        return

    N = inputs[0] # Ngoc's line
    M = inputs[1] # Minh's line

    n_size = len(N)
    m_size = len(M)
    
    candy_n = 0
    candy_m = 0

    p_n = 0
    p_m = 0

    while p_n < n_size and p_m < m_size:
        c_n = N[p_n] 
        c_m = M[p_m] 

        if c_n == c_m:
            candy_n += 1
            candy_m += 1
            p_n += 1
            p_m += 1
        elif (c_n == 'R' and c_m == 'G') or (c_n == 'G' and c_m == 'B') or (c_n == 'B' and c_m == 'R'):
            candy_n += 1
            p_m += 1
        else:
            candy_m += 1
            p_n += 1

    if p_n < n_size:
        candy_n += (n_size - p_n)
    if p_m < m_size:
        candy_m += (m_size - p_m)

    print(candy_n)
    print(candy_m)

if __name__ == '__main__':
    function()
