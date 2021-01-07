############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#          Project : 307multigrains        #
#                                          #
############################################

from copy import deepcopy

from sources.Matrix import Matrix

class Multigrains():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self):
        self._total = 0
        self._grains = {'Oat':      [1, 1, 2, 0],
                        'Wheat':    [0, 2, 1, 0],
                        'Corn':     [1, 0, 0, 3],
                        'Barley':   [0, 1, 1, 1],
                        'Soy':      [2, 0, 0, 2]}
        self._ressources = [0, 0, 0, 0]
        self._prices = [0, 0, 0, 0, 0]
        self._production = [0, 0, 0, 0, 0]

    def parse(self, argv: list) -> None:

        """Parse the input arguments."""

        self._ressources[0] = int(argv[1])
        self._ressources[1] = int(argv[2])
        self._ressources[2] = int(argv[3])
        self._ressources[3] = int(argv[4])
        self._prices[0] = int(argv[5])
        self._prices[1] = int(argv[6])
        self._prices[2] = int(argv[7])
        self._prices[3] = int(argv[8])
        self._prices[4] = int(argv[9])

    def display(self) -> None:

        def displayProduction(i=0) -> None:
            for grain in self._grains:
                if self._production[i] == 0:
                    print(f"{grain}: 0 units at ${self._prices[i]}/unit")
                else:
                    print("{}: {:.2f} units at ${}/unit".format(
                            grain, self._production[i], self._prices[i]))
                i += 1

        print(f"Resources: {self._ressources[0]} F1, {self._ressources[1]} F2, {self._ressources[2]} F3, {self._ressources[3]} F4")
        print()
        displayProduction()
        print()
        print("Total production value: ${:.2f}".format(self._total))

    def applyPrices(self, products: list, matrix: Matrix) -> None:

        for i in range(4):
            if products[i] != -1:
                if matrix._matrix[i][-1] != 0:
                    self._total += matrix._matrix[i][-1] * self._prices[products[i]]
                self._production[products[i]] = matrix._matrix[i][-1]

    def compute(self) -> None:

        """Compute productions quota for each grain type.
        """

        matrix = Matrix({"n1": self._ressources[0], "n2": self._ressources[1], "n3": self._ressources[2],
                        "n4": self._ressources[3], "po": self._prices[0], "pw": self._prices[1],
                        "pc": self._prices[2], "pb":self._prices[3], "ps": self._prices[4]})

        products = [-1, -1, -1, -1]

        for i in range(5):
            pivot_x, pivot_y = matrix.getPivot()
            if pivot_x < 0 or pivot_y < 0:
                break
            matrix.applyPivot(pivot_x, pivot_y)
            products[pivot_y] = pivot_x
        self.applyPrices(products, matrix)

    def run(self, argv: list) -> None:

        """
        Run computations and process output printing.
        """

        self.parse(argv)
        self.compute()
        self.display()
