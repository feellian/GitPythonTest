#!/usr/bin/env python
import os
import unittest
import subprocess

from git import *
from py_git_test import *


class GitUnlock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.environ['PATH'] += ':' + os.path.abspath(
            os.path.join(os.path.dirname(__file__), ".."))

    def setUp(self):
        self.git = GitTest()
        self.git.create_file('.git/index.lock')

    def tearDown(self):
        self.git.clean()

    def test_git_unlock(self):
        run_bash('git-unlock')
        assert not os.path.exists('.git/index.lock')

    def test_git_unlock_twice(self):
        try:
            run_bash('git-unlock')
            run_bash('git-unlock')
        except OSError:
            pass
        else:
            self.fail("expected an OSError exception")


    def test_git_unlock_exec(self):
        result = run_bash('git-unlock -e echo')
        self.assertEquals(result.strip(), '.git/index.lock')

        result = run_bash('git-unlock --exec echo')
        self.assertEquals(result.strip(), '.git/index.lock')

if __name__ == '__main__':
    unittest.main()
