"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2  # Assuming a fixed preparation time of 2 minutes per layer

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(layers):
    """Calculate the preparation time in minutes.

    :param layers: int - number of lasagna layers.
    :return: int - total preparation time derived from 'PREPARATION_TIME' per layer.
    """
    return layers * PREPARATION_TIME

def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """Calculate the total elapsed time in minutes.

    :param layers: int - number of lasagna layers.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time (in minutes) for preparation and baking.
    """
    return preparation_time_in_minutes(layers) + elapsed_bake_time

#  (you can copy and then alter the one from bake_time_remaining.)
