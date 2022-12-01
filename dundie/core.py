""" Core module of Dundie Soft
This module contains the main programs`s functions"""


def load(filepath):
    """Loads data from filepath to the DB"""
    try:
        with open(filepath) as file_:
            return file_.readlines()
    except FileNotFoundError as e:
        print(e)
