############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#             Project : 303make            #
#                                          #
############################################

class ArgumentManager():

    def checkArgs(self, argv) -> int:

        """
        Check for input arguments validity.
        """

        def isFile(filename: str) -> bool:

            """Check if filename is an existing file."""

            try:
                f = open(filename)
            except IOError:
                print("{} is not a valid file.".format(filename))
                return False
            else:
                f.close()
                return True

        if len(argv) != 2 and len(argv) != 3:
            print("Wrong number of arguments.")
            return 84
        elif not isFile(argv[1]):
            return 84
        else:
            return 0

    def needHelp(self, argv) -> bool:

        """
        Check if the user is asking for help.
        """

        if "-h" in argv or "--help" in argv:
            return True
        return False
