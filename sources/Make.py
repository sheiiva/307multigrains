############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#             Project : 303make            #
#                                          #
############################################

from sources.Parser import Parser
from sources.Matrix import Matrix

class Make():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self, argv):
        self._makefile = None
        self._file = None
        #
        self.parseArguments(argv)

    def parseArguments(self, argv: list) -> None:
        """Parse input arguments into class attributes.

        Args:
            argv (list): Input arguments.
        """

        self._makefile = argv[1]
        if len(argv) == 3:
            self._file = argv[2]

    def readFiles(self, filename: str) -> list:
        """Read and get the input file content.

        Args:
            filename (str): file to be readen.

        Returns:
            list: List of strings (each file line is a string)
        """

        content = []

        with open(filename) as file: 
            lines = file.readlines() 
            for line in lines:
                line = line.replace('\n', '')
                content.append(line)
        # Remove empty elements
        while '' in content:
            content.remove('')
        if len(content) == 0:
            print("Makefile is empty.")
            exit(84)
        return content

    def printRuleDependencies(self, matrix: list, dependencies: list, elements: list) -> None:
        """Print rules and dependencies from matrix.

        Args:
            matrix (list): Adjacency matrix
            dependencies (list): Rules and its dependencies
            elements (list): All existing elements of the Makefile
        """
        def findDependencyPath(matrix, elements, rawIndex, dependencies, index):
            dependencies.append(elements[rawIndex])
            for i in range(index, len(matrix[rawIndex])):
                if matrix[rawIndex][i] == 1:
                    findDependencyPath(matrix, elements, i, dependencies, 0)
                    return

        def printDependecies(dependencies: list) -> None:
            for i in range(len(dependencies)):
                print(dependencies[i], end='')
                if i < (len(dependencies)-1):
                    print(" -> ", end='')
                else:
                    print()

        for j in range(len(matrix)):
            for i in range(len(matrix[j])):
                if matrix[j][i] == 1:
                    dependencies = []
                    findDependencyPath(matrix, elements, j, dependencies, i)
                    printDependecies(dependencies)

    def printCommands(self, fileContent: str, elements: list, dependencies: list) -> None:

        def getCommands(commands: list, fileContent: str, target: str, dependencies: list) -> None:

            for i in range(len(fileContent)):
                if ':' in fileContent[i] and fileContent[i+1] not in commands:
                    rule, currentTarget = fileContent[i].split(':')
                    if target in currentTarget.split():
                        commands.append(fileContent[i+1])
                        getCommands(commands, fileContent, rule, dependencies)

        commands = []
        getCommands(commands, fileContent, self._file, dependencies)
        commands.sort()

        if self._file not in elements:
            print("{} not in {}".format(self._file, self._makefile))
            exit(84)
        if len(commands) == 0:
            print()
        else:
            [print(command) for command in commands]


    def run(self) -> None:

        """
        Run computations and process output printing.
        """

        # PARSER
        parser = Parser()
        fileContent = self.readFiles(self._makefile)
        elements, depedencies = parser.parseInput(fileContent)

        # MATRIX
        matrix = Matrix()
        m = matrix.create(len(elements))
        m = matrix.fill(m, elements, depedencies)

        # OUTPUT PRINTING
        if self._file is None:
            matrix.print(m)
            print()
            self.printRuleDependencies(m, depedencies, elements)
        else:
            self.printCommands(fileContent, elements, depedencies)