#!/usr/bin/env python3
############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#             Project : 303make            #
#                                          #
############################################


from sys import argv

from sources.Usage import Usage
from sources.ArgumentManager import ArgumentManager
from sources.Make import Make


def main():

    argsManager = ArgumentManager()

    if argsManager.needHelp(argv):
        Usage()
    elif argsManager.checkArgs(argv) == 84:
        exit(84)
    else:
        Make(argv).run()


if __name__ == "__main__":
    main()
