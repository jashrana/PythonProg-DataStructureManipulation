# I/we declare that this file represents our own work, and that we
# have not seen any work on this assignment done by others, and that
# we have not shown our work to any others.

# Student name(s): Soumitra Koustubh Manavi, Jash Prakash Rana
# Student ID(s): 22220805, 22222806

# Do not change the formatting above. For multiple names/IDs, use
# commas to separate.


from collections import Counter


def dict_sort(d):
    result = {}
    for k in sorted(d.keys()):
        # in modern Python, dicts remember the order in which their keys
        # were added, and use that order when being printed
        result[k] = d[k]
    return result


def count_treasure(box):
    '''
    While wandering in the fortress of the goblin king, we've discovered a
    box of treasure!

    Count all the treasure and other items in the box and return the
    result as a `dict`, with keys sorted alphabetically.
    
    `box` is a `dict` specifying the number of each item, eg:
    >>> count_treasure({'coins': 10, 'diamonds': 10})
    {'coins': 10, 'diamonds': 10}

    The above is a box containing 10 coins and 10 diamonds, so the output
    is as shown.

    A container (the box itself, or a bag, pouch, etc.) can contain other
    containers. Instead of a number, the containers are specified as a 
    list, tuple, or similar. We should include the containers in the count:
    >>> count_treasure({'coins': 10,  
    ...                 'bags': [{'coins': 2}, {'coins': 5}]})
    {'bags': 2, 'coins': 17}

    Notice the above is a multi-line doctest, using ...

    Containers can be recursive:
    >>> count_treasure({'bags': [{'bags': [{'coins': 10}]}]})
    {'bags': 2, 'coins': 10}

    Here is a bigger example:
    >>> count_treasure({
    ...   'coins': 10,
    ...   'rubies': 10,
    ...   'enchanted pouches': [{
    ...      'coins': 10,
    ...      'rubies': 10,
    ...      'treasure chests': (
    ...         {'coins': 1000},
    ...         {'coins': 1000},
    ...         {'coins': 1000}
    ...      ) # this was a tuple of 3 treasure chests
    ...    }] # this was a list of 1 enchanted pouches
    ... })
    {'coins': 3020, 'enchanted pouches': 1, 'rubies': 20, 'treasure chests': 3}

    If the input is mis-specified, we expect to see an error:
    >>> count_treasure({'bags': (10, 20, 30)})
    Traceback (most recent call last):
    ...
    TypeError: 'int' object is not iterable
    '''

    # HINT: use a `Counter` to store your results while working
    result = Counter()
    ## YOUR CODE HERE

    def rec_func(k_box, v_box):
        # checking the value from dictionary if it is a tuple or a list
        if isinstance(v_box, (list, tuple)):
            # Counter stores and updates the results
            result.update({k_box: len(v_box)})
            for elements in v_box:
                if isinstance(elements, dict):
                    for k1, v1 in elements.items():
                        rec_func(k1, v1)
                elif isinstance(elements, int):
                    # raises exception : TypeError: 'int' object is not iterable
                    result.update(elements)
        # checking the value if it contains a dictionary
        elif isinstance(v_box, dict):
            result.update({k_box: len(v_box)})
            for k2, v2 in v_box.items():
                rec_func(k2, v2)
        # if the value is integer, it updates the result wrt key
        else:
            result.update({k_box: v_box})

    #for loop to iterate through box which is a dictionary
    for k_box, v_box in box.items():
        #calls recursive function
        rec_func(k_box, v_box)

    # HINT: use `dict_sort(result)` at the end to sort and
    # convert to an ordinary `dict`
    return dict_sort(result)
