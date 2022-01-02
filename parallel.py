import random
import multiprocessing as mp


def create_data(x, y):
    data = [[random.randint(1, 20) for i in range(y)] for j in range(x)]
    return data


def sum_row(row):
    sum = 0
    for index, e in enumerate(row):
        sum += e
        row[index] = sum
    return row


def transpose_matrix(matrix):
    # https://stackoverflow.com/questions/6473679/transpose-list-of-lists
    return list(map(list, zip(*matrix)))


def main():
    data = create_data(5, 10)
    print(data)
    num_processes = mp.cpu_count()
    pool = mp.Pool(processes=num_processes)
    result = pool.map(sum_row, data)
    print(result)



if __name__ == '__main__':
    main()
