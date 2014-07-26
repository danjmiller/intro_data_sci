import MapReduce
import sys


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: text of the document
    key = record[0]
    text = record[1]
    words = text.split()
    for w in words:
      mr.emit_intermediate(w,key)

def reducer(key, list_of_values):
    # key: word
    # value: list of document ids

    de_duped = []
    for document in list_of_values:
        if document not in de_duped:
            de_duped.append(document)

    mr.emit((key, de_duped))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
