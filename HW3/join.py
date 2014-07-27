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
    # value: columns from order and line item tables

    orders = []
    line_items = []

    for cols in list_of_values:
        if cols[0] == "order":
            orders.append(cols)
        else:
            line_items.append(cols)

    for order in orders:
        for line_item in line_items:
            mr.emit(order + line_item)


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)

