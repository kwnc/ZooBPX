import random
import numpy as np


def normalize(x, x_min, x_max):
    '''
    Normalizacja danych - zmiana zakresu cechy z pozostawieniem proporcji miedzy wartosciami
    :param x: instancja cechy wszystkich zwierzat
    :param x_min: najmniejsza wartosc cechy zwierzat
    :param x_max: najwieksza wartosc cechy zwierzat
    :return: znormalizowana cecha
    '''
    for idv, val in enumerate(x):
        x[idv] = (2 * (val - x_min)) / (x_max - x_min) - 1
    return x


def prepare_data(sort):
    '''
    Losowe wczytanie danych bez kolumny "animal_name" do tabeli numpy
    W transpozycji normalizacja cech bez parametru gatunek(type)
    Podzielenie danych na trenujace/testujace (80%/20%)
    :param sort: bool czy dane mają zostać posortowane czy nie
    :return:
    '''
    with open("data/zoo.txt") as file:
        data = [list(map(float, x.strip().split(',')[1:])) for x in file]

    test_data = []
    tab = []

    random.shuffle(data)
    data = np.asarray(data)
    data = data.transpose()
    for k in range(16):
        data[k] = normalize(data[k], np.min(data[k]), np.max(data[k]))
    data = data.transpose()
    tile = [8, 4, 1, 2, 1, 2, 2]
    for k in range(1, 8):
        ile = 0
        for m, val in enumerate(data):
            if val[16] == k:
                ile += 1
                tab.append(m)
                test_data.append(val)
            if ile == tile[k-1]:
                break
    data = np.delete(data, tab, 0)
    if sort:
        data = data[np.argsort(data[:, 16])]
    test_data = np.asarray(test_data)
    test_data = test_data[np.argsort(test_data[:, 16])]
    data = data.transpose()
    test_data = test_data.transpose()
    return [data, test_data]
