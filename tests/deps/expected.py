############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#             Project : 303make            #
#                                          #
############################################


HELP_MESSAGE = "\
USAGE\n\
\t./303make makefile [file]\n\
DESCRIPTION\n\
\tmakefile\tname of the makefile\n\
\tfile\t\tname of a recently modified file\n"

NORMAL_CASE = "\
[0 0 1 0 0 0]\n\
[0 0 1 0 0 1]\n\
[0 0 0 1 0 0]\n\
[0 0 0 0 0 0]\n\
[0 0 0 0 0 1]\n\
[0 0 0 1 0 0]\n\
\n\
fc.c -> fc.o -> tty\n\
fc.h -> fc.o -> tty\n\
fc.h -> tty.o -> tty\n\
fc.o -> tty\n\
tty.c -> tty.o -> tty\n\
tty.o -> tty\n"

TTY_C_CASE="\
cc -c tty.c\n\
cc -o tty tty.o fc.o\n"

FC_H_CASE="\
cc -c fc.c\n\
cc -c tty.c\n\
cc -o tty tty.o fc.o\n"