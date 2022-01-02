import random
import multiprocessing as mp
import time
from itertools import chain


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
    num_processes = mp.cpu_count()
    pool = mp.Pool(processes=num_processes)

    chunk_size = int(len(data)/num_processes)
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    data_row_summed = pool.map(sum_chunk, chunks)

    transposed = transpose_matrix(data_row_summed)
    transposed = list(chain.from_iterable(transposed))

    chunk_size = int(len(transposed)/num_processes)
    chunks = [transposed[i:i + chunk_size] for i in range(0, len(transposed), chunk_size)]

    data_col_summed = pool.map(sum_chunk, chunks)
    final = transpose_matrix(data_col_summed)

    end_time = time.time()
    print(f'Completed in {end_time - start_time:.2f} secs.')


if __name__ == '__main__':
    main()
