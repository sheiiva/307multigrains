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


def test_arguments_ok():

    argMan = ArgumentManager()

    argv = ['./307multigrains', '45', '41', '21', '63', '198', '259', '257', '231', '312']

    assert argMan.checkArgs(argv) != 84


def test_wrong_number_args(capsys):

    argMan = ArgumentManager()

    argv = ['./307multigrains', '45', '21', '63', '198', '259', '257', '231', '312']
    assert argMan.checkArgs(argv) == 84

    redir = capsys.readouterr()
    assert redir.out == "ERROR: wrong number of arguments.\n"


def test_not_digit(capsys):

    argMan = ArgumentManager()

    argv = ['./307multigrains', '45', 'a', '21', '63', '198', '259', '257', '231', '312']
    assert argMan.checkArgs(argv) == 84

    redir = capsys.readouterr()
    assert redir.out == "ERROR: arguments might be integers.\n"


def test_negative_value(capsys):

    argMan = ArgumentManager()

    argv = ['./307multigrains', '45', '-3838', '21', '63', '198', '259', '257', '231', '312']
    assert argMan.checkArgs(argv) == 84

    redir = capsys.readouterr()
    assert redir.out == "ERROR: arguments might be positive values.\n"


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
