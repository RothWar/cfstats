
"""
2016-08-29 Christoph Haarburger

Analyze Crossfit testing week results
"""

import csv


class Athlete:
    """
    Basic class representing results for an athlete and testing week
    """
    def __init__(self, d):
        """
        Initialize athlete with scores dictionary

        Parameters:
        d : dictionary containing workout scores as generated in read_csv

        Returns:
        None
        """
        self.scores = d

    def print_stats(self, workout=None):
        """
        Print athlete scores to command line

        Parameters:
        workout : name of workout to be printed

        Returns:
        None
        """
        if workout is None:
            for w, s in sorted(self.scores.items()):
                print(w + ": " + s)
        elif workout in self.scores.keys():
            print(workout + ": " + self.scores[workout])
        else:
            raise ValueError("unknown workout")


def read_csv(file):
    """
    Read scores from CSV file and create list of Athlete objects

    Parameters:
    file : path to CSV file

    Returns:
    athlete_list : list of Athlete objects with corresponding workout scores
    """

    athlete_list = []
    with open(file, 'r') as mycsvfile:
        dictofdata = csv.DictReader(mycsvfile, delimiter=";")
        for athlete_dict in dictofdata:
            a = Athlete(athlete_dict)
            a.print_stats()
            athlete_list.append(a)
    return athlete_list

file = 'testing_week_1.csv'
athlete_list = read_csv(file)
