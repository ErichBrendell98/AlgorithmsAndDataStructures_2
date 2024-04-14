import pytest
from closest_value import  *
from bst import *


@pytest.fixture(scope="session")
def data():
    array = [[10, 5, 15, 13, 22, 14, 2, 5, 1],
             [100,5,502,204,55000,1001,4500,203,205,207,
              206,208,2,15,5,22,57,60,1,3,-51,1,1,1,1,1,-403]
             ]
    return array


def test_1(data):
    bst = BST()
    for value in data[0]:
        bst.add(value)
    assert findClosestValue(bst, 12) == 13


def test_2(data):
    bst = BST()
    for value in data[1]:
        bst.add(value)
    assert findClosestValue(bst, 100) == 100


def test_3(data):
    bst = BST()
    for value in data[1]:
        bst.add(value)
    assert findClosestValue(bst, 208) == 208


def test_4(data):
    bst = BST()
    for value in data[1]:
        bst.add(value)
    assert findClosestValue(bst, 4500) == 4500


def test_5(data):
    bst = BST()
    for value in data[1]:
        bst.add(value)
    assert findClosestValue(bst, 4501) == 4500


def test_6(data):
    bst = BST()
    for value in data[1]:
        bst.add(value)
    assert findClosestValue(bst, -70) == -51


def test_7(data):
    bst = BST()
    for value in data[1]:
        bst.add(value)
    assert findClosestValue(bst, 2000) == 1001


def test_8(data):
    bst = BST()
    for value in data[1]:
        bst.add(value)
    assert findClosestValue(bst, 6) == 5


def test_9(data):
    bst = BST()
    for value in data[1]:
        bst.add(value)
    assert findClosestValue(bst, 30000) == 55000


def test_10(data):
    bst = BST()
    for value in data[1]:
        bst.add(value)
    assert findClosestValue(bst, -1) == 1


def test_11(data):
    bst = BST()
    for value in data[1]:
        bst.add(value)
    assert findClosestValue(bst, 29751) == 55000


def test_12(data):
    bst = BST()
    for value in data[1]:
        bst.add(value)
    assert findClosestValue(bst, 29749) == 4500