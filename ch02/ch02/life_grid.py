from ch02.array import Array2D

class LifeGrid:
    DEAD_CELL = 0
    LIVE_CELL = 1

    def __init__(self, rows, cols):
        """Creates a new game grid cosisting of rows and cols.
        All cells in the grid are set to dead."""
        # Allocate the 2-D array for the grid
        self._grid = Array2D(numRows, numCols)
        # clear the grid and set all cells to dead.i
        self.configure(list())

    def numRows(self):
        """Returns the num of rows"""
        return self._grid.numRows()

    def numCols(self):
        """Return the number of columns in the grid."""
        return self._grid.numCols()

    def configure(self, coordList):
        """Configures the grid for evolving the next generation.
        The coordList argument is a sequence of 2-tuples with each
        tuple representing the coordinates (r,c) of the cells to be set as alive.
        All remaining cells are cleared or set to dead."""
        # clear the game grid
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self.clearCell(i, j)

        # set the indicated cells to be alive
        for coord in coordList:
            self.setCell(coord[0], coord[1])

    def clearCell(self, row, col):
        """Clears the individual cell (row, col) to be alive.
        The cell indices must be within the valid range of the grid."""
        self._grid[row, col] = self.DEAD_CELL

    def setCell(self, row, col):
        """Sets the indicated cell (row, col) and sets (row, col) to be alive. The
        cell indices must be within the valid range of the grid."""
        self._grid[row, col] = self.LIVE_CELL

    def isLiveCell(self, row, col):
        """Returns a boolean value indicating if the given cell (row, col) contains a live oraganism.
        The cell indices must be withing the valid range of the grid."""
        return self._grid[row, col] == self.LIVE_CELL

    def numLiveNeighbors(self, row, col):
        """Returns the number of live neighbors for the given cell (row, col).
        The neighbors of a cell include all the cells immediately surrounding it in all directions.
        For the cells along the border of the grid, the neighbors that fall outside the grid are assumed to be dead.
        The cell indices must be within the balid range of the grid."""

