import time
import multiprocessing


# job 1
def counter1(num):
    count = 0
    for _ in range(num):
        count += 1
    print("Counter1 Done!!!")


# job 2
def counter2(num):
    count = 0
    for _ in range(0, num, 2):
        count += 1
    print("Counter2 Done!!!")


if __name__ == "__main__":
    # single processing
    N = 2 * 10**8
    start = time.time()
    counter1(N)
    counter2(N)
    end = time.time()

    print(f"Time taken: {end-start}")

    # multi processing
    start = time.time()
    # initialize the job1
    job1 = multiprocessing.Process(target=counter1, args=(N,))

    # initialize the job2
    job2 = multiprocessing.Process(target=counter2, args=(N,))

    # start the jobs
    job1.start()
    job2.start()

    # join the jobs
    job1.join()
    job2.join()
    end = time.time()
    print(f"Time taken: {end-start}")
