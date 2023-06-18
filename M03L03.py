import numpy
from numpy.linalg import matrix_rank
import random


class VectorSpace:
    def __init__ (self, path):
        file = open(path, "r")
        pre_matrix = []
        for line in file:
            pre_vector = line.split(',')
            for point_index in range(len(pre_vector)):
                pre_vector[point_index] = float(pre_vector[point_index].strip())
            pre_matrix.append(pre_vector)

        self.path = path
        self.matrix = numpy.matrix(pre_matrix).transpose()
        self.rank = matrix_rank(self.matrix)
        self.ort = numpy.linalg.qr(self.matrix)[0].transpose()*(-1)

    def details (self, path):
        file = open(path, "w")

        file.write("Rank: {}\n".format(self.rank))
        file.write("Ort matrix: {}\n".format(list(self.ort)))

    def sum (self, other):
        return numpy.matrix([].append(list(self.matrix)).append(list(other.matrix)))

    def isin (self, point):
        return bool(round(random.random()))


custom_vector_space = VectorSpace('M03L03_input.txt')
custom_vector_space.details('M03L03_output.txt')

# for debug
#print(custom_vector_space.rank)
#print(custom_vector_space.matrix)
#print(list(custom_vector_space.ort))
