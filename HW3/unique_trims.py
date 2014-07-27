import MapReduce
import sys


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: sequence, minus the last 10 characters
    # value: nothing, we don't need this
    sequence = record[1]

    #don't bother adding a value, only care about the key
    mr.emit_intermediate(sequence[:-10], " ")


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts

    mr.emit(key)
    # Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)

