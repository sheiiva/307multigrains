############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#          Project : 307multigrains        #
#                                          #
############################################

class ArgumentManager():

    def checkArgs(self, argv) -> int:

        """
        Check for input arguments validity.
        """

        def isInt(va) -> bool:
            try:
                int(va)
            except ValueError:
                return False
            else:
                return True

        if len(argv) != 10:
            print("ERROR: wrong number of arguments.")
            return 84
        for arg in argv[1:]:
            if isInt(arg) is False:
                print("ERROR: arguments might be integers.")
                return 84
            if int(arg) < 0:
                print("ERROR: arguments might be positive values.")
                return 84

    def needHelp(self, argv) -> bool:

        """
        Check if the user is asking for help.
        """

        if "-h" in argv or "--help" in argv:
            return True
        return False
