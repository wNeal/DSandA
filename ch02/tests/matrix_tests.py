from nose.tools import *
from ch02.array import Matrix

def test_scale():
    m = Matrix(3, 3)
    count = 1
    for r in range(m.numRows()):
        for c in range(m.numCols()):
            m[r, c] = count
            count += 1

    # Scale the matrix by 2
    m.scale_by(2)
    assert_equal(m[0, 0], 2, "incorrect scaling {0} =/= {1}".format(m[0, 0], 2))
    assert_equal(m[0, 1], 4, "incorrect scaling {0} =/= {1}".format(m[0, 1], 4))
    assert_equal(m[0, 2], 6, "incorrect scaling {0} =/= {1}".format(m[0, 2], 6))
    assert_equal(m[1, 0], 8, "incorrect scaling {0} =/= {1}".format(m[1, 0], 8))
    assert_equal(m[1, 1], 10, "incorrect scaling {0} =/= {1}".format(m[1, 1], 10))
    assert_equal(m[1, 2], 12, "incorrect scaling {0} =/= {1}".format(m[1, 2], 12))
    assert_equal(m[2, 0], 14, "incorrect scaling {0} =/= {1}".format(m[2, 0], 14))
    assert_equal(m[2, 1], 16, "incorrect scaling {0} =/= {1}".format(m[2, 1], 16))
    assert_equal(m[2, 2], 18, "incorrect scaling {0} =/= {1}".format(m[2, 2], 18))

def test_transpose():
    """
    [1,2,3] >> [1,3]
    [3,2,1] >> [2,2]
               [3,1]
    """
    m = Matrix(2,3)
    m[0, 0] = 1
    m[0, 1] = 2
    m[0, 2] = 3
    m[1, 0] = 3
    m[1, 1] = 2
    m[1, 2] = 1

    transposed_matrix = m.transpose()
    assert_equal(transposed_matrix.numRows(), m.numCols(), "incorrect matrix dimensions")
    assert_equal(transposed_matrix.numCols(), m.numRows(), "incorrect matrix dimensions")
    assert_equal(transposed_matrix[0, 0], 1, "value mismatch")
    assert_equal(transposed_matrix[0, 1], 3, "value mismatch")
    assert_equal(transposed_matrix[1, 0], 2, "value mismatch")
    assert_equal(transposed_matrix[1, 1], 2, "value mismatch")
    assert_equal(transposed_matrix[2, 0], 3, "value mismatch")
    assert_equal(transposed_matrix[2, 1], 1, "value mismatch")
