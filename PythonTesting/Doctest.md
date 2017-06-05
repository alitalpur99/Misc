The *doctest* module is often considered easier to use than the *unittest*, though the later is more suitable for more complex tests. 
doctest is a test framework that comes prepackaged with Python. The doctest module searches for pieces of text that look like
interactive Python sessions inside of the documentation parts of a module, and then executes (or reexecutes) the commands of those
sessions to verify that they work exactly as shown, i.e. that the same results can be achieved. In other words: The help text of
the module is parsed for example python sessions. These examples are run and the results are compared against the expected value. 

Usage of doctest: 
To use "doctest" it has to be imported. The part of an interactive Python sessions with the examples and the output has to 
be copied inside of the docstring the corresponding function. 

We demonstrate this by Cube function here (refer *cube_doctest.py* file).

We copy the complete session of the interactive shell into the docstring of our function. To start the module doctest we have to 
call the method testmod(), but only if the module is called standalone. The complete module looks like this now:


```
"""Testing using Doctest"""

def cube(n):
    """
    >>> cube(2)
    8
    >>> cube(5)
    125
    >>> cube(6)
    216
    >>> cube(7)
    343"""
    return n**3

if __name__ == "__main__": 
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)
```


Output is shown below:

```
OUTPUT OF THE ABOVE cube_doctest.py

Trying:
    cube(2)
Expecting:
    8
ok
Trying:
    cube(5)
Expecting:
    125
ok
Trying:
    cube(6)
Expecting:
    216
ok
Trying:
    cube(7)
Expecting:
    343
ok
1 items had no tests:
    __main__
1 items passed all tests:
   4 tests in __main__.cube
4 tests in 2 items.
4 passed and 0 failed.
Test passed.
>>> 
```

If we start our module directly `$ python3 cube_doctest.py` without doctest.testmod additional parameters, we get no output, 
because everything is okay. 

To see how doctest works, if something is wrong, we place an error in our code: 

We change again `return n**3` into `return n**2`

Now we get the following, if we start our module:
```
Trying:
    cube(2)
Expecting:
    8
**********************************************************************
File "test.py", line 5, in __main__.cube
Failed example:
    cube(2)
Expected:
    8
Got:
    4
Trying:
    cube(5)
Expecting:
    125
**********************************************************************
File "test.py", line 7, in __main__.cube
Failed example:
    cube(5)
Expected:
    125
Got:
    25
Trying:
    cube(6)
Expecting:
    216
**********************************************************************
File "test.py", line 9, in __main__.cube
Failed example:
    cube(6)
Expected:
    216
Got:
    36
Trying:
    cube(7)
Expecting:
    343
**********************************************************************
File "test.py", line 11, in __main__.cube
Failed example:
    cube(7)
Expected:
    343
Got:
    49
1 items had no tests:
    __main__
**********************************************************************
1 items had failures:
   4 of   4 in __main__.cube
4 tests in 2 items.
0 passed and 4 failed.
***Test Failed*** 4 failures.
>>>
```
Now we are getting Square instead of Cube of the number. All four test will fail. The output depicts all the calls, which return 
faulty results. We can see the call with the arguments in the line following 
"Failed example:". We can see the expected value for the argument in the line following "Expected:". The output shows us the
newly calculated value as well. We can find this value behind "Got:" 
