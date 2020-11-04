#! /usr/bin/env python3
import pytest
import glob
import sys
from test_expect_pragma import TestExpectPragmas

ALL_FILES = glob.glob('./testfiles/test*.txt')


ARIT_EVAL = 'arit1.py'


class TestEVAL(TestExpectPragmas):
    def evaluate(self, file):
        return self.run_command(['python3', ARIT_EVAL, file])

    @pytest.mark.parametrize('filename', ALL_FILES)
    def test_expect(self, filename):
        expect = self.get_expect(filename)
        eval = self.evaluate(filename)
        assert expect == eval


if __name__ == '__main__':
    pytest.main(sys.argv)
