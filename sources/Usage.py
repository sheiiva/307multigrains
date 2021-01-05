############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#             Project : 303make            #
#                                          #
############################################

class Usage():

    def __init__(self):
        self.show()

    def show(self) -> None:

        """
        Show usage of the program.
        """

        print(
            "USAGE\n"
            "\t./303make makefile [file]\n"
            "DESCRIPTION\n"
            "\tmakefile\tname of the makefile\n"
            "\tfile\t\tname of a recently modified file"
            )
