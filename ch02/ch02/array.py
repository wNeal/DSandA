import ctypes

class Array :
    """Implements the Array ADT using array capabilities of the ctypes module."""
    def __init__( self, size ):
        """Creates an array with size elements."""
        assert size > 0, "Array size must be > 0"
        self._size = size

        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()

        # Initialize each element.
        self.clear( None )

    def __len__( self ):
        """Returns the size of the array."""
        return self._size

    def __getitem__( self, index ):
        """Gets the contents of the index element."""
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[ index ]

    def __setitem__( self, index, value ):
        """Puts the value in the array element at index position."""
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[ index ] = value

    def clear( self, value ):
        """Clears the array by setting each element to the given value."""
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__( self ):
        """Returns the array's iterator for traversing the elements."""
        return _ArrayIterator( self._elements )



class Array2D :
    """Implementation of the Array2D ADT using an array of arrays."""
    def __init__( self, numRows, numCols ):
        """Creates a 2-D array of size numRows x numCols."""
        # Create a 1-D array to store an array reference for each row.
        self._theRows = Array( numRows )

        # Create the 1-D arrays for each row of the 2-D array.
        for i in range( numRows ) :
            self._theRows[i] = Array( numCols )

    def numRows( self ):
        """Returns the number of rows in the 2-D array."""
        return len( self._theRows )

    def numCols( self ):
        """Returns the number of columns in the 2-D array."""
        return len( self._theRows[0] )

    def clear( self, value ):
        """Clears the array by setting every element to the given value."""
        for row in range( self.numRows() ):
            self._theRows[row].clear( value )


    def __getitem__( self, ndxTuple ):
        """Gets the contents of the element at position [i, j]"""
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]

        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), \
        "Array subscript out of range."
        the1dArray = self._theRows[row]
        return the1dArray[col]

    def __setitem__( self, ndxTuple, value ):
        """Sets the contents of the element at position [i,j] to value."""
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]

        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), \
        "Array subscript out of range."
        the1dArray = self._theRows[row]
        the1dArray[col] = value

class Matrix:
    """A matrix is a collection of scalar values arranged in rows and columns as a
    rectangular grid of a fixed size. The elements of the matrix can be accessed by specifying
    a given row and column index with indices starting at 0.
    """
    def __init__(self, rows, cols):
        """Creates a new matrix containing rows and columns with each element initialized to 0"""
        self._theGrid = Array2D(rows, cols)
        self._theGrid.clear(0)

    def numRows(self):
        """Returns the number of rows in the matrix"""
        return self._theGrid.numRows()

    def numCols(self):
        """Returns the number of columns in the matrix"""
        return self._theGrid.numCols()

    def __getitem__(self, i):
        """Returns the value stored in the given matrix element. Both row and col must be within the
        valid range."""
        return self._theGrid[i[0], i[1]]

    def __setitem__(self, i, scalar):
        """Sets the matrix element at the given row and col to scalar. The element indices must be
        within the valid range."""
        self._theGrid[i[0], i[1]] = scalar

    def scale_by(self, scalar):
        """Multiplies each element of the matrix by the given scalar value. The matrix is modified
        by this operation"""
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self[r,c] *= scalar

    def transpose(self):
        """Returns a new matrix that is the transpose of this matrix"""
        new_matrix = Matrix(self.numCols(), self.numRows())
        for col in range(self.numCols()):
            for row in range(self.numRows()):
                new_matrix[col, row] = self._theGrid[row, col]

        return new_matrix

    def __add__(self, rhsMatrix):
        """Creates and returns a new matrix that is the result of adding this matrix to the given rhsMatrix.
        The size of the two matrices must be the same"""
        assert rhsMatrix.numRows() == self.numRows() and \
                rhsMatrix.numCols == self.numRows(), \
                "Matrix sizes are not compatible for the add operation."
        # Create the new matrix
        newMatrix = Matrix(self.numRows(), self.numCols())
        # Add the corresponding elements in the two matrices
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r,c] = self[r,c] + rhsMatrix[r,c]
        return newMatrix

    def __sub__(self, rhsMatrix):
        """The same as add() operation but subtracts the two matrices."""

    def __mul__(self, rhsMatrix):
        """Creates and returns a new matrix that is the result of mulitplying this matrix to the given
        rhsMatrix. The two matrices must be of appropriate sizes as defined for matrix multiplication.
        """

class _ArrayIterator :
    """An iterator for the Array ADT."""
    def __init__( self, theArray ):
        self._arrayRef = theArray
        self._curNdx = 0

    def __iter__( self ):
        return self

    def __next__( self ):
        if self._curNdx < len( self._arrayRef ) :
            entry = self._arrayRef[ self._curNdx ]
            self._curNdx += 1
            return entry
        else :
            raise StopIteration
