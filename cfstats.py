
"""
2016-08-29 Christoph Haarburger

Analyze Crossfit testing week results
"""

import csv
from datetime import datetime


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
        # convert strings containing times to datetime
        for workout in ["helen", "open_16.5", "row_500m", "row_5000m",
                        "airbike_100cal"]:
            if self.scores[workout] is not "":
                self.scores[workout] = datetime.strptime(self.scores[workout],
                                                         "%M:%S").time()

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
                print(w + ": " + str(s))
        elif workout in self.scores.keys():
            print(workout + ": " + str(self.scores[workout]))
        else:
            raise ValueError("unknown workout")


def read_csv(csv_file):
    """
    Read scores from CSV file and create list of Athlete objects

    Parameters:
    csv_file : path to CSV file

    Returns:
    athlete_list : list of Athlete objects with corresponding workout scores
    """

    athlete_list = []
    with open(csv_file, 'r') as mycsvfile:
        dictofdata = csv.DictReader(mycsvfile, delimiter=";")
        for athlete_dict in dictofdata:
            a = Athlete(athlete_dict)
            a.print_stats()
            athlete_list.append(a)
    return athlete_list

csv_file = 'testing_week_1.csv'
athlete_list = read_csv(csv_file)
