import json
from random import choice


def generator():
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'p', 'l', 'm', 'n', 'o', 'i']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    while len(name) != 8:
        name += choice(letters)
        tel += choice(numbers)

    return {"Name": name, "Phone": tel}


def load_data(data):
    try:
        file_data = json.load(open('persons.json'))
    except:
        file_data = []

    file_data.append(data)

    with open('persons.json', 'w') as f:
        json.dump(file_data, f, indent=2, ensure_ascii=False)


def main():
    for i in range(5):
        load_data(generator())


if __name__ == '__main__':
    main()
