"""
Unit and regression test for the arthritis_proj package.
"""

import os
import shutil
import sys
import tempfile
import unittest
from contextlib import contextmanager
from io import StringIO
import os.path

import numpy as np

from arthritis_proj import main, DEFAULT_DATA_FILE_LOC, data_analysis, DATA_DIR


class TestMain(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()
        os.chdir(self.test_dir)

    def tearDown(self):
        # Remove the directory after the test
        os.chdir(os.path.dirname(__file__))
        shutil.rmtree(self.test_dir)

    def testNoArgs(self):
        test_input = []
        main(test_input)
        with capture_stdout(main, test_input) as output:
            self.assertTrue("sample_data_stats.csv" in output)

        self.assertTrue(os.path.isfile("sample_data_stats.csv"))
        self.assertTrue(os.path.isfile("sample_data_stats.png"))

    def testMissingFile(self):
            test_input = ["-c", "ghost.txt"]
            main(test_input)
            with capture_stderr(main, test_input) as output:
                self.assertTrue("ghost.txt" in output)


class TestDataAnalysis(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()
        os.chdir(self.test_dir)

    def tearDown(self):
        # Remove the directory after the test
        os.chdir(os.path.dirname(__file__))
        shutil.rmtree(self.test_dir)

    def testSampleData(self):
        csv_data = np.loadtxt(fname=DEFAULT_DATA_FILE_LOC, delimiter=',')
        analysis_results = data_analysis(csv_data)
        expected_results = np.loadtxt(fname=os.path.join(DATA_DIR, "sample_data_results.csv"), delimiter=',')
        self.assertTrue(np.allclose(expected_results, analysis_results))

    def testSampleData2(self):
        csv_data = np.loadtxt(fname=os.path.join(DATA_DIR, "sample_data2.csv"), delimiter=',')
        analysis_results = data_analysis(csv_data)
        expected_results = np.loadtxt(fname=os.path.join(DATA_DIR, "sample_data2_results.csv"), delimiter=',')
        self.assertTrue(np.allclose(expected_results, analysis_results))


# Utility functions

# From http://schinckel.net/2013/04/15/capture-and-test-sys.stdout-sys.stderr-in-unittest.testcase/
@contextmanager
def capture_stdout(command, *args, **kwargs):
    # pycharm doesn't know six very well, so ignore the false warning
    # noinspection PyCallingNonCallable
    out, sys.stdout = sys.stdout, StringIO()
    command(*args, **kwargs)
    sys.stdout.seek(0)
    yield sys.stdout.read()
    sys.stdout = out

@contextmanager
def capture_stderr(command, *args, **kwargs):
    # pycharm doesn't know six very well, so ignore the false warning
    # noinspection PyCallingNonCallable
    err, sys.stderr = sys.stderr, StringIO()
    command(*args, **kwargs)
    sys.stderr.seek(0)
    yield sys.stderr.read()
    sys.stderr = err