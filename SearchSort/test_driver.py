from pytest import *
from Sort import *


# Test Sorting
class TestSorting:

    # initialize an instance of Set for each test
    def setup_method(self, method):
        self.input1 =[
            [],
            [1], 
            [1,2], 
            [2,1], 
            [1,2,3], 
            [3,2,1],
            [1,1,1],
            [4,2,1,3]]
        self.ans1 = [
            [],
            [1], 
            [1,2], 
            [1,2], 
            [1,2,3], 
            [1,2,3],
            [1,1,1],
            [1,2,3,4]]

    # reset state variables
    def teardown_method(self, method):
        self.input1 = None

    def test_sorting(self):
        assert list(map(bufferSort, self.input1)) == self.ans1
