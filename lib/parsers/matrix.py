import json

def parse(string_array):
    converted = []
    latex_matrix = ""
    matrix = json.loads(string_array)
    converted.append(r"$\begin{pmatrix}")
    if(len(matrix) > 1):
        for i in range(0, len(matrix) - 1):
            sub_matrix = matrix[i]
            row = ""
            row = row + str(sub_matrix[0])
            for j in range(1, len(sub_matrix)):
                row = row + r" & " + str(sub_matrix[j])
            row = row + r"\\"
            converted.append(row)
    sub_matrix = matrix[len(matrix) - 1]
    row = ""
    row = row + str(sub_matrix[0])
    for j in range(1, len(sub_matrix)):
        row = row + r" & " + str(sub_matrix[j])
    converted.append(row)
    converted.append(r"\end{pmatrix}$")
    for row in converted:
        latex_matrix = latex_matrix + row + '\n'
    return latex_matrix