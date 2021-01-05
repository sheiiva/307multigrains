############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#           Project : 301dannon            #
#                                          #
############################################

import pytest

from sources.ArgumentManager import ArgumentManager


def test_ok_1_arguments(capsys):

    argMan = ArgumentManager()

    argv = ['./303make', 'Makefile']

    assert argMan.checkArgs(argv) == 0


def test_ok_2_arguments(capsys):

    argMan = ArgumentManager()

    argv = ['./303make', 'Makefile', 'arg']

    assert argMan.checkArgs(argv) == 0


def test_ko_wrong_nb_args(capsys):

    argMan = ArgumentManager()

    argv = ['./303make']

    assert argMan.checkArgs(argv) == 84
    stdout, _ = capsys.readouterr()

    excepted = "Wrong number of arguments.\n"
    assert stdout == excepted


def test_ko_arg_not_a_file(capsys):

    argMan = ArgumentManager()

    argv = ['./303make', 'notFile', 'arg']

    assert argMan.checkArgs(argv) == 84
    stdout, _ = capsys.readouterr()

    excepted = "{} is not a valid file.\n".format(argv[1])
    assert stdout == excepted


def test_needHelp_h():

    argMan = ArgumentManager()

    argv = ['./303make', '-h']

    assert argMan.needHelp(argv) is True


def test_needHelp_help():

    argMan = ArgumentManager()

    argv = ['./303make', '--help']

    assert argMan.needHelp(argv) is True


def test_needHelp_wrong_case():

    argMan = ArgumentManager()

    argv = ['./303make', 'no']

    assert argMan.needHelp(argv) is False
