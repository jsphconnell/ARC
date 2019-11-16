import json


def read_json(file_path):
    """
    Function to read a json file into a data dictionary structure
    :param file_path: Path and name of json file to read
    :return: A data dictionary with the json content as dict

    >>> read_json('./data/test/test_puzzle.json')
    {'train': [{'input': [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]], 'output': [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]}, {'input': [[0, 0, 0, 8, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]], 'output': [[0, 0, 0, 8, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 4, 0, 4, 0]]}], 'test': [{'input': [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]], 'output': [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 7, 0, 0]]}]}

    """
    with open(file_path) as json_file:
        data_dict = json.load(json_file)
    return data_dict


def read_input_samples(data_dict):
    """
    Function that takes only the input property from the dictionary
    Ignores train or test and just takes all inputs as equal
    :param data_dict: data dictionary with the full file input structure loaded
    :return: a dictionary of just input values

    >>> dict = {'train': [{'input': [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]], 'output': [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]}, {'input': [[0, 0, 0, 8, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]], 'output': [[0, 0, 0, 8, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 4, 0, 4, 0]]}], 'test': [{'input': [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]], 'output': [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 7, 0, 0]]}]}
    >>> read_input_samples(dict)
    {0: [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]], 1: [[0, 0, 0, 8, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]], 2: [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]}

    """
    inputs_dict = {}
    i = 0
    for train_inputs in data_dict["train"]:
        inputs_dict[i] = train_inputs["input"]
        i += 1

    for test_inputs in data_dict["test"]:
        inputs_dict[i] = test_inputs["input"]
        i += 1

    return inputs_dict


if __name__ == "__main__":
    import doctest
    doctest.testmod()