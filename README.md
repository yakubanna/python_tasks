# python_tasks
Solving simple python tasks

LABYRINTHS1 is the solution of the problem:
There is a labyrinth given by the cell field, in which w rows and h columns. The mouse is initially located in a cell with coordinates (x, y). It can move along the cell borders to the left, right, up and down, if there is no barrier in the cell and it does not climb to the border. It is necessary for each cell (i, j) of the labyrinth to find the length of the minimum path from the cell (x, y) or to determine that it is impossible to get to this cell.

DINNER_HELPER is the solution of the problem:
N silent philosophers sit around the round table, before each philosopher stands a plate of spaghetti. Forks lie on the table between each pair of the closest philosophers.
Every philosopher can either eat or think. Food intake is not limited to the amount of spaghetti left - an infinite supply is implied. Nevertheless, a philosopher can eat only when he holds two forks - taken from the right and left.
Each philosopher can take the nearest fork (if available), or put - if he already holds it. Taking each fork and returning it to the table are separate actions that must be performed one after another.
The essence of the problem is to develop a model of behavior (parallel algorithm), in which none of the philosophers will not starve, that is, they will always alternate meals and reflections (the philosopher should start with reflection).

EXTENDED_DICT is the solution of the problem:
It is necessary to write the ExtendedDict class, which will be inherited from the standard dict and will support the following additional features:

    The keys of the ExtendedDict class object can only be strings, an attempt to set a non-string key or to get a value on a non-string key should result in the ValueError   
    Setting the value by key through setting the attribute (that is, for an object in the ExtendedDict class, you could make a.key = value, which is equivalent.    
    Deleting a value by key by removing an attribute (that is, for an object in the ExtendedDict class, del a.key could be made, which is equivalent.    
    The ExtendedDict class should support the syntax of the slices, i.e. a slice of an object of the ExtendedDict class should return the corresponding slice of the list of pairs (key, value) sorted by the key (it is not necessary to support the slice syntax for changing the object)
    
    
LIFE_EMULATION is the solution of the problem:
We need to write a LifeEmulation class that models the modification of the game "Life". The game is a two-dimensional field, in each cell of which a non-negative number is written. In our modification there are the following conditions for the "development" and "degradation" of cells:

    an empty cell, or a cell with a value of 0, receives a value of 1, provided that it is surrounded by 3 cells with a value greater than 0;
    a cell with a value greater than 0 will "grow", that is, it will get +1, provided it has 2-3 neighbors with a value greater than 0;
    a cell with a value greater than 0 will take the value 0 if it has 1, 4-5 neighbors having a value above 0;
    a cell with a value above 0 will "degrade", that is, its value will decrease by 1 (-1), provided that all neighboring cells have 0, or 6 or 8 neighbors have a value greater than 0.

In addition, there is a limit of cell growth, i. E. The value of the cell can not increase if it reaches a certain threshold.
The following interface is expected from your class:

    A constructor that takes a two-dimensional array of the starting state and the limit of cell growth;
    a method of converting an object into a string that returns strings representing the rows of the field, separated by a line break (unix-style), the numbers in the row are separated by a space;
    a method that returns the neighbors' indices for the cell (i, j);
    a method that returns the number of neighbors for a cell (i, j) with a positive value;
    a method that returns the next state for the cell (i, j), but does not change the cell itself;
    the iterate method, which produces one iteration of all cell states
    An attribute that must return a two-dimensional array of the current state of the field.
    
    
ROME_TO_ARABIC is the solution of the problem:
Given a number written in the Roman numeral system. You need to write a function that translates it into a decimal number system.


SPOON is the solution of the problem: It is required to write an interpreter for the isoteric language Spoon (https://ru.wikipedia.org/wiki/Spoon). Running: python3 spoon.py path_to_spoon_code_file.
IMPORTANT! If the read operation from the standard input stream returns EOF, then this should be treated as writing to the cell of code 0.
We assume that the cells can store signed numbers up to 4 bytes, but if a command is issued to output the value in the cell, then there must be a one-byte value, otherwise we consider this situation undefined behaviour.
It is assumed that a valid file containing the Spoon code without delimiters (alphabet 0/1) will be fed to the input.

 
