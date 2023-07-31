# Python Programming Basics - Data Structures Manipulation
To run, use `python -m doctest <filename>.py` for doctest results

1. Counting Treasures<br>
While wandering in the fortress of the goblin king, we've discovered a
box of treasure!

Count all the treasure and other items in the box and return the
result as a `dict`, with keys sorted alphabetically.

`box` is a `dict` specifying the number of each item, eg:
>>> count_treasure({'coins': 10, 'diamonds': 10})<br>
`{'coins': 10, 'diamonds': 10}`

The above is a box containing 10 coins and 10 diamonds, so the output
is as shown.

A container (the box itself, or a bag, pouch, etc.) can contain other
containers. Instead of a number, the containers are specified as a 
list, tuple, or similar. We should include the containers in the count:
>>> count_treasure({'coins': 10,<br>
>>> 'bags': [{'coins': 2}, {'coins': 5}]})
`{'bags': 2, 'coins': 17}`

Notice the above is a multi-line doctest, using ...

Containers can be recursive:
>>> count_treasure({'bags': [{'bags': [{'coins': 10}]}]})
{'bags': 2, 'coins': 10}

Here is a bigger example:

>>> count_treasure({<br>
>>> 'coins': 10,<br>
>>> 'rubies': 10,<br>
>>> 'enchanted pouches': [{<br>
>>> 'coins': 10,<br>
>>> 'rubies': 10,<br>
>>> 'treasure chests': (<br>
>>> {'coins': 1000},<br>
>>> {'coins': 1000},<br>
>>> {'coins': 1000}<br>
>>> ) # this was a tuple of 3 treasure chests<br>
>>> }] # this was a list of 1 enchanted pouches<br>
>>> })<br>
`{'coins': 3020, 'enchanted pouches': 1, 'rubies': 20, 'treasure chests': 3}`

If the input is mis-specified, we expect to see an error:
>>> count_treasure({'bags': (10, 20, 30)})<br>
`Traceback (most recent call last):
...
TypeError: 'int' object is not iterable`

HINT: use a `Counter` to store your results while working.<br><br>

2. Draw Treasures<br>
Draw a simple picture on a grid.

A picture is specified as a list of shapes. Each shape is either a
`disc` or a `rect`.

`draw` creates the grid as a list of lists and draws the shapes.

A second function, `render`, takes care of some details of
printing correctly.

The coordinate system starts at the top-left of the image.
