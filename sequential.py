import random
import multiprocessing as mp
import time


def create_data(x, y):
    random.seed(42)
    data = [[random.randint(1, 20) for i in range(y)] for j in range(x)]
    return data


def sum_chunk(chunk):
    for f in chunk:
        sum = 0
        for index, e in enumerate(f):
            sum += e
            f[index] = sum
    return chunk


def transpose_matrix(matrix):
    # https://stackoverflow.com/questions/6473679/transpose-list-of-lists
    return list(map(list, zip(*matrix)))


def main():
    data = create_data(10000, 10000)

    start_time = time.time()

    data = sum_chunk(data)
    transposed = transpose_matrix(data)
    transposed = sum_chunk(transposed)
    final = transpose_matrix(transposed)

    end_time = time.time()
    print(f'Completed in {end_time - start_time:.2f} secs.')


if __name__ == '__main__':
    main()

