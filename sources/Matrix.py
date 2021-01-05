############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#             Project : 303make            #
#                                          #
############################################

class Matrix():

    """
    Matrix management and creation.
    """

    def create(self, size: int) -> list:
        """Create a size*size sized matrix

        Args:
            size (int): Size of the matrix.

        Returns:
            list: 0 filled matrix.
        """

        return [[0 for _ in range(size)] for _ in range(size)]

    def fill(self, matrix: list, elements: list, dependencies: list) -> list:

        for rules in dependencies:
            for target in rules[-1]:
                matrix[elements.index(target)][elements.index(rules[0])] = 1

        return matrix

    def print(self, matrix: list) -> None:
        """Formatted output printing of a matrix.

        Args:
            matrix (list): Matrix to print.
        """

        for raw in matrix:
            print('[', end='')
            for i in range(len(raw)):
                print(raw[i], end='')
                if i < len(raw) - 1:
                    print(' ', end='')
            print(']')
