############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#             Project : 303make            #
#                                          #
############################################

class Parser():

    """
    Parse arguments and input files.
    """

    def __init__(self):
        self._makefile = None

    def parseInput(self, makefileContent: list) -> (list, list):
        """Parse the makefile content into dependencies list.

        Args:
            makefileContent (list): Makefile content.
        """

        def getDependecies(makefileContent: str) -> list:

            depencies = []

            for line in makefileContent:
                if ':' in line:
                    rule, target = line.split(':')
                    # Split and clean targets
                    target = target.split()
                    while '' in target:
                        target.remove('')
                    depencies.append([rule, target])
            return depencies

        def getElements(makefileContent: str) -> list:

            elements = []

            def cleanLine(line: str) -> str:
                line = line.replace('\n', '')
                line = line.replace(':', '')
                line = line.replace('cc -o', '')
                line = line.replace('cc -c', '')
                return line.lstrip().rstrip()


            for line in makefileContent:
                line = cleanLine(line)
                tmp = line.split()
                for element in tmp:
                    if element not in elements:
                        elements.append(element)
            elements.sort()
            return elements

        return getElements(makefileContent), getDependecies(makefileContent)