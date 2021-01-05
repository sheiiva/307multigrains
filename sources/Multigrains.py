############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#          Project : 307multigrains        #
#                                          #
############################################

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
                        'Soy':      [2, 0, 0 , 2]}
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
                print(f"{grain}: {self._production[i]} units at ${self._prices[i]}/unit")
                i += 1

        print(f"Resources: {self._ressources[0]} F1, {self._ressources[1]} F2, {self._ressources[2]} F3, {self._ressources[3]} F4")
        print()
        displayProduction()
        print()
        print("Total production value: ${:.2f}".format(self._total))

    def run(self, argv: list) -> None:

        """
        Run computations and process output printing.
        """

        self.parse(argv)
        # self.compute()
        self.display()