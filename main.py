import numpy as np
import logging

FORMAT = '{levelname} - {asctime} {msg}'
logging.basicConfig(filename='logs.log', level=logging.INFO, filemode="w", format=FORMAT, style='{')
log = logging.getLogger(__name__)


class Matrix:

    def __init__(self, martix1: list, matrix2: list):

        CORRECT_TYPE = type(np.array([]))
        if type(martix1) == CORRECT_TYPE and type(matrix2) == CORRECT_TYPE:
            self.matrix1 = martix1
            self.matrix2 = matrix2
        else:
            log.error(f'An argument in the constructor of an instance of the "Matrix" class mast be "numpy.ndarray",'
                      f' but actually "martix1" is {type(martix1)}, "matrix2" is {type(matrix2)}')

    def __repr__(self):
        return print(f'{self.matrix1, self.matrix2}')

    def summ_matrixs(self) -> list:
        """Метод возвращает сумму двух матриц, созданных с помощью библиотеки numpy"""
        sum_of_matrices = self.matrix1 + self.matrix2
        log.info(f'The result of the function "summ_matrixs" will be {sum_of_matrices}:')
        return sum_of_matrices

    def equal_matrixs(self) -> bool:
        """Метод сравнивает две матрицы, созданных с помощью библиотеки numpy"""
        is_equal_matrix = np.array_equal(self.matrix1, self.matrix2)
        log.info(f'The result of the function "equal_matrixs" will be "{is_equal_matrix}"')
        return is_equal_matrix


if __name__ == '__main__':
    MAT1 = np.array([[1, 3, 4], [11, 21, 31]])
    MAT2 = np.array([[4, 1, 26], [5, -2, 10]])
    exemplar = Matrix(MAT1, MAT2)
    result_matrix = exemplar.summ_matrixs()
    is_equal = exemplar.equal_matrixs()
    print(result_matrix)
    print(is_equal)
