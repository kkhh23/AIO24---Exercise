def count_word(file_path):
    result = {}
    with open(file_path, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                word = word.lower()
                if word in result:
                    result[word] += 1
                else:
                    result[word] = 1
    return result