import math
import multiprocessing
import time

# without multiprocessing


def check_prime(N):
    arr = [True]*N
    for num in range(N):
        if num < 2:
            arr[num] = False
        elif num > 2:
            for i in range(2, math.ceil(math.sqrt(num))+1):
                if num % i == 0:
                    arr[num] = False
                    break
    return arr

# with multiprocessing


def check_prime_multiprocessing(N):
    if N < 2:
        return N, False
    elif N == 2:
        return True
    else:
        for i in range(2, math.ceil(math.sqrt(num))+1):
            if N % i == 0:
                return N, False
    return N, True


if __name__ == "__main__":
    # single processing
    start = time.time()
    N = 2 * 10 * 8
    check_prime(N)
    end = time.time()
    print(f"Time taken: {end - start}")
