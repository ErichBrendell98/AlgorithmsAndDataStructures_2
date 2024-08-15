import pytest
from bst import BST
from kth_largest_value import findKthLargestValue


@pytest.fixture(scope="session")
def data():

    array = [[15,5,20,17,22,2,5,1,3],
             [5,4,6,3,7],
             [5],
             [20,15,25,10,19,21,30,22],
             [1,2,3,4,5],
             [10,8,6,4,2],
             [10,8,6,9,4,7,2,5,3],
             [99727,99,727],
             [15,5,20,17,22,24,23,25,2,5,1,3],
             [15,5,20,17,22,2,5,1,3],
             [15,5,20,17,22,2,5,1,3]
             ]
    return array

def test_1(data):
    bst = BST()
    for value in data[0]:
        bst.add(value)
    assert findKthLargestValue(bst, 3) == 17

def test_2(data):
    bst = BST()
    for value in data[1]:
        bst.add(value)
    assert findKthLargestValue(bst, 1) == 7

def test_3(data):
    bst = BST()
    for value in data[2]:
        bst.add(value)
    assert findKthLargestValue(bst, 1) == 5

def test_4(data):
    bst = BST()
    for value in data[3]:
        bst.add(value)
    assert findKthLargestValue(bst, 3) == 22

def test_5(data):
    bst = BST()
    for value in data[4]:
        bst.add(value)
    assert findKthLargestValue(bst, 5) == 1

def test_6(data):
    bst = BST()
    for value in data[5]:
        bst.add(value)
    assert findKthLargestValue(bst, 2) == 8

def test_7(data):
    bst = BST()
    for value in data[6]:
        bst.add(value)
    assert findKthLargestValue(bst, 5) == 6

def test_8(data):
    bst = BST()
    for value in data[7]:
        bst.add(value)
    assert findKthLargestValue(bst, 1) == 99727

def test_9(data):
    bst = BST()
    for value in data[8]:
        bst.add(value)
    assert findKthLargestValue(bst, 7) == 15

def test_10(data):
    bst = BST()
    for value in data[9]:
        bst.add(value)
    assert findKthLargestValue(bst, 5) == 5

def test_11(data):
    bst = BST()
    for value in data[10]:
        bst.add(value)
    assert findKthLargestValue(bst, 6) == 5
