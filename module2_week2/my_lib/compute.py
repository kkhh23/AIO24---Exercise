import numpy as np


def compute_vector_length(vector):
    result = np.linalg.norm(vector)
    return result


def compute_dot_product(v1, v2):
    result = np.dot(v1, v2)
    return result


def matrix_multi_vector(matrix, vector):
    result = np.dot(matrix, vector)
    return result


def matrix_multi_matrix(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result


def inverse_matrix(matrix):
    result = np.linalg.inv(matrix)
    return result


def compute_eigenvalues_eigenvectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors


def compute_cosine(v1, v2):
    result = compute_dot_product(v1, v2)/(compute_vector_length(v1)*compute_vector_length(v2))
    return result
