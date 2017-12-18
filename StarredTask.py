def make_dict(keys, values):
    dictionary = dict()
    for i in range(len(keys)):
        if i > len(values) - 1:
            dictionary.update({keys[i]: None})
        else:
            dictionary.update({keys[i]: values[i]})

    return dictionary


if __name__ == "__main__":
    keys = [1, 2, 3, 4, 5]
    values = ['one', 'two', 'three']
    print(make_dict(keys, values))
