def character_count(str):
    dict_ = {}
    # a = str.lower()
    for i in str:
        if i in dict_:
            dict_[i] += 1
        else:
            dict_[i] = 1
    return dict_


assert character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
print(character_count('smiles'))
