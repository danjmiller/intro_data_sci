import MapReduce
import sys


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    if record[0] == 'a':
        i = record[1]
        j = record[2]
        a_ij = record[3]

        for k in range(5):
            key = (i, k)
            value = ('a', j, a_ij)
            mr.emit_intermediate(key, value)

    else:
        j = record[1]
        k = record[2]
        b_jk = record[3]

        for i in range(5):
            key = (i,k)
            value = ('b', j, b_jk)
            mr.emit_intermediate(key,value)


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts

    a_cells = {}
    b_cells = {}

    # split the A and B into separate dictionaries
    for cell in list_of_values:
        if cell[0] == 'a':
            a_cells[cell[1]] = cell[2]
        else:
            b_cells[cell[1]] = cell[2]

    sum = 0

    for j in range(5):
        if not a_cells.has_key(j):
            a_cells[j] = 0
        if not b_cells.has_key(j):
            b_cells[j] = 0

        sum += a_cells[j] * b_cells[j]

    mr.emit((key[0], key[1], sum))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)

