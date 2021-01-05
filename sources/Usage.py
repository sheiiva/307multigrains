############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#          Project : 307multigrains        #
#                                          #
############################################

class Usage():

    def __init__(self):
        self.show()

    def show(self) -> None:

        """
        Show usage of the program.
        """

        print("USAGE\n"
            "\t./307multigrains n1 n2 n3 n4 po pw pc pb ps\n"
            "\n"
            "DESCRIPTION\n"
            "\tn1\tnumber of tons of fertilizer F1\n"
            "\tn2\tnumber of tons of fertilizer F2\n"
            "\tn3\tnumber of tons of fertilizer F3\n"
            "\tn4\tnumber of tons of fertilizer F4\n"
            "\tpo\tprice of one unit of oat\n"
            "\tpw\tprice of one unit of wheat\n"
            "\tpc\tprice of one unit of corn\n"
            "\tpb\tprice of one unit of barley\n"
            "\tps\tprice of one unit of soy"
            )
