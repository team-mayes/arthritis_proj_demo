"""
data_proc.py
Demo including processing data from a csv

Handles the primary functions
"""

import sys
import argparse
import numpy as np

SUCCESS = 0
IO_ERROR = 2

DEF_DATA_FILE = 'data.csv'


def warning(*objs):
    """Writes a message to stderr."""
    print("WARNING: ", *objs, file=sys.stderr)


def data_analysis(data_array):
    """
    Finds the average, min, and max for each row of the given array

    Parameters
    ----------
    data_array : numpy array of patient data (one line per patient, daily measurements) in plasma inflammation units

    Returns
    -------
    data_stats : numpy array
        array with same number of rows as data_array, and columns for average, max, and min values (in that order)
    """
    print(type(data_array))
    print(data_array)
    num_patients, num_days = data_array.shape

    data_stats = np.zeros((num_patients, 3))
    return data_stats


def parse_cmdline(argv):
    """
    Returns the parsed argument list and return code.
    `argv` is a list of arguments, or `None` for ``sys.argv[1:]``.
    """
    if argv is None:
        argv = sys.argv[1:]

    # initialize the parser object:
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--csv_data_file", help="The location of the csv file with data to analyze",
                        default=DEF_DATA_FILE)
    args = None
    try:
        args = parser.parse_args(argv)
        args.csv_data = np.loadtxt(fname=args.csv_data_file, delimiter=',')
    except IOError as e:
        warning("Problems reading file:", e)
        parser.print_help()
        return args, IO_ERROR

    return args, SUCCESS


def main(argv=None):
    args, ret = parse_cmdline(argv)
    if ret != SUCCESS:
        return ret
    data_stats = data_analysis(args.csv_data)
    print(data_stats)
    return SUCCESS  # success


if __name__ == "__main__":
    status = main()
    sys.exit(status)
