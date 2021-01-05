303make
===

Time:       2 weeks

Team:       1

Language:   Python


The project
----
As you know, when compiling a program, only the files that are dependent on recently modified sources are effectively recompiled during a [**Make function call**](https://www.gnu.org/software/make/manual/html_node/Functions.html). In order to do this, this binary parses the **Makefile** in the current folder so that a dependency graph can be generated.Next, it analyzes this graph in order to execute the **minimum amount of compilations**.


In this project you must simulate the behavior of Make by reconstructing the dependency graph, and then **display all of the commands to be executed** after a source file is modified.First, you’ll need to display the adjacency matrix and the dependency strings.


## USAGE:

```
>> ./303make -h
USAGE
    ./303make makefile [file]
DESCRIPTION
    makefile    name of the makefile
    file        name of a recently modified file
```

Author [**Corentin COUTRET-ROZET**](https://github.com/sheiiva)