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

from sources.Multigrains import Multigrains
from tests.deps.expected import *


def tests_ok_case_1(capsys):

    argv = ['./307multigrains', '10', '100', '10', '0', '200', '200', '200', '200', '200']
    Multigrains().run(argv)

    redir = capsys.readouterr()

    assert redir.out == CASE_1_OUTPUT


def tests_ok_case_2(capsys):

    argv = ['./307multigrains', '45', '41', '21', '63', '198', '259', '257', '231', '312']
    Multigrains().run(argv)

    redir = capsys.readouterr()

    assert redir.out == CASE_2_OUTPUT