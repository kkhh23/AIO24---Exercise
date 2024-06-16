def levenshtein_distance(source, target):

    # create table for check distance
    distances = [[0 for x in range(len(target)+1)] for y in range(len(source)+1)]

    # create 1st row
    for i in range(len(source)+1):
        distances[i][0] = i

    # create 1st col
    for j in range(len(target)+1):
        distances[0][j] = j

    for i in range(1, len(source)+1):
        for j in range(1, len(target)+1):
            """
            Note:
            If source[i] == target[j]:
            subcost(source[i] ,target[j])=0
            """
            if source[i - 1] == target[j - 1]:
                distances[i][j] = distances[i-1][j-1]
            else:
                del_cost = distances[i-1][j] + 1
                ins_cost = distances[i][j - 1] + 1
                sub_cost = distances[i-1][j-1] + 1
                distances[i][j] = min(del_cost,ins_cost,sub_cost)

    return distances[len(source)][len(target)]
