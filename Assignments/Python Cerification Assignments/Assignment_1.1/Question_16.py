# Q16. Python program to find the power of a number using recursion.

def power(N, P):

    if P == 0:
        return 1
    else: 
        return (N*power(N, P-1))

if __name__ == '__main__':
    N = int(input())
    P = int(input())
    print(power(N, P))