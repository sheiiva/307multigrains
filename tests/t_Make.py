############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#             Project : 303make            #
#                                          #
############################################

import pytest

from sources.Make import Make
from tests.deps.expected import *


def tests_normal_case(capsys):

    argv = ['./303make', 'tests/deps/MakefileTest']
    Make(argv).run()

    redir = capsys.readouterr()

    assert redir.out == NORMAL_CASE


def tests_tty_c_case(capsys):

    argv = ['./303make', 'tests/deps/MakefileTest', 'tty.c']
    Make(argv).run()

    redir = capsys.readouterr()

    assert redir.out == TTY_C_CASE


def tests_fc_h_case(capsys):

    argv = ['./303make', 'tests/deps/MakefileTest', 'fc.h']
    Make(argv).run()

    redir = capsys.readouterr()

    assert redir.out == FC_H_CASE


def tests_binary_case(capsys):

    argv = ['./303make', 'tests/deps/MakefileTest', 'tty']
    Make(argv).run()

    redir = capsys.readouterr()

    assert redir.out == "\n"


def tests_item_not_in_file(capsys):

    argv = ['./303make', 'tests/deps/MakefileTest', 'notIntFile']

    try:
        Make(argv).run()
    except SystemExit:
        redir = capsys.readouterr()
        assert redir.out == "notIntFile not in tests/deps/MakefileTest\n"
    else:
        assert 0 == 1 # The tests failed.


def tests_empty_file(capsys):

    argv = ['./303make', 'tests/deps/emptyMakefile']

    try:
        Make(argv).run()
    except SystemExit:
        redir = capsys.readouterr()
        assert redir.out == "Makefile is empty.\n"
    else:
        assert 0 == 1 # The tests failed.