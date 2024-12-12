import random

def generate_random_array(size):
    return [str(random.randint(0, 10000)) for _ in range(size)]

array_size = 1000
dummy_array = generate_random_array(array_size)


def write_file(data, file_path):
    with open(file_path, 'w+') as f:
        f.write(','.join(data))

write_file(dummy_array, './static/array.txt')
