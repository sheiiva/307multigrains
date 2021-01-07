############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#          Project : 307multigrains        #
#                                          #
############################################

import pytest

from sources.ArgumentManager import ArgumentManager


# def test_ok_1_arguments(capsys):

#     argMan = ArgumentManager()

#     argv = ['./307multigrains', 'Makefile']

#     assert argMan.checkArgs(argv) == 0

def test_needHelp_h():

    argMan = ArgumentManager()

    argv = ['./307multigrains', '-h']

    assert argMan.needHelp(argv) is True


def test_needHelp_help():

    argMan = ArgumentManager()

    argv = ['./307multigrains', '--help']

    assert argMan.needHelp(argv) is True


def test_needHelp_wrong_case():

    argMan = ArgumentManager()

    argv = ['./307multigrains', 'no']

    assert argMan.needHelp(argv) is False
