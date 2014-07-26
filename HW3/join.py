import MapReduce
import sys


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order id
    # value: table name + table columns
    order_id = record[1]

    mr.emit_intermediate(order_id, record)


def reducer(key, list_of_values):
    # key: order id
    # value: list of columns
    total = 0
    for v in list_of_values:
        total += v
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)

