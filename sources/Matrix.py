############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#          Project : 307multigrains        #
#                                          #
############################################

class Matrix():

    """
    Matrix class that allows matrix handling, computation and output printing.
    """

    def __init__(self, infos: dict):
        self._matrix = self.createMatrix(infos)

    def createMatrix(self, infos: dict) -> list:

        """Create a matrix filled with the input values."""

        matrix = []

        matrix.append([1, 0, 1, 0, 2, 1, 0, 0, 0, infos["n1"]])
        matrix.append([1, 2, 0, 1, 0, 0, 1, 0, 0, infos["n2"]])
        matrix.append([2, 1, 0, 1, 0, 0, 0, 1, 0, infos["n3"]])
        matrix.append([0, 0, 3, 1, 2, 0, 0, 0, 1, infos["n4"]])
        matrix.append([-infos["po"], -infos["pw"], -infos["pc"], -infos["pb"], -infos["ps"], 0, 0, 0, 0, 0])

        return matrix

    def getPivot(self) -> tuple:

        """Get for matrix pivot.

        Returns:
            dict: pivot coordinates such as {x: value, y: value}
        """

        maxy = 5
        maxx = 10

        prices = self.getPrices()
        
        minPrice = min(prices)

        y = -1
        x = prices.index(minPrice)
        #
        minPrice = 99999999999999

        for i in range(maxy):

            if self._matrix[i][maxx -1]:
                if self._matrix[i][x] > 0 and (minPrice > self._matrix[i][maxx - 1] / self._matrix[i][x]
                                                and self._matrix[i][maxx - 1] / self._matrix[i][x] > 0):
                    y = i
                    minPrice = self._matrix[i][maxx - 1] / self._matrix[i][x]
            elif minPrice > self._matrix[i][x] and self._matrix[i][x] > 0:
                y = i
                minPrice = self._matrix[i][maxx - 1] / self._matrix[i][x]

        return (x, y)

    def applyPivot(self, xpivot: int, ypivot: int) -> None:

        """Apply pivot to the Matrix

        Args:
            pivot_x (int): X coordinates of the pivot
            pivot_y (int): Y coordinates of the pivot
        """

        pivotValue = self._matrix[ypivot][xpivot]

        for i in range(len(self._matrix[ypivot])):
            self._matrix[ypivot][i] /= pivotValue

        maxx = 10
        maxy = 5

        for i in range(maxy):
            if i == ypivot:
                continue
            k = self._matrix[i][xpivot]
            for j in range(maxx):
                self._matrix[i][j] -= k * self._matrix[ypivot][j]

    def getPrices(self) -> list:

        return self._matrix[-1][:5]
