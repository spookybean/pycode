def data_generator(num_values):
    for i in range(num_values):
        data = {
            'id': i * 4
        }
        yield data


for i in data_generator(20):
    print(i)