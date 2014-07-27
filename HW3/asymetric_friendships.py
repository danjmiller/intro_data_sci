import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person name
    # value: friend
    person = record[0]
    friend = record[1]
    mr.emit_intermediate(person, friend)
    mr.emit_intermediate(friend, person)


def reducer(key, list_of_values):
    # key: person
    # value: list of friend counts

    unique_people = set(list_of_values)

    for person in unique_people:
        if list_of_values.count(person) == 1
            mr.emit((key, person))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
