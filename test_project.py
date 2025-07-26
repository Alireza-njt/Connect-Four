# Alireza Nejati (alirezanejatiz27@gmail.com)
# Saturday , July 26 , 2025
# Course name : CS50's Introduction to Programming with Python
# Final project name : Connect Four

from cs50Python.week9.project import *
from pytest import raises


def test_initial_state():
    assert initial_state() == [[Empty for _ in range(7)] for _ in range(6)]
    assert initial_state(3, 3) == [[Empty for _ in range(3)] for _ in range(3)]
    assert initial_state(4, 4) == [[Empty for _ in range(4)] for _ in range(4)]
    assert initial_state(rows=10, cols=15) == [[Empty for _ in range(15)] for _ in range(10)]


def test_actions():
    assert actions([[]], rows=0, cols=0) == []
    assert actions([[Empty, Empty, Empty], [Empty, Empty, Empty], [Empty, Empty, Empty]],
                   rows=3, cols=3) == [(0, 2), (1, 2), (2, 2)]
    assert actions([[Empty, Empty, Empty], [Empty, Empty, Empty], [Empty, Empty, Yellow]],
                   rows=3, cols=3) == [(0, 2), (1, 2), (2, 1)]
    assert actions([[Empty, Empty, Red], [Empty, Red, Yellow], [Red, Yellow, Red]],
                   rows=3, cols=3) == [(0, 1), (1, 0)]

    with raises(IndexError):
        assert actions([[Empty, Empty, Empty], [Empty, Empty, Empty],
                       [Empty, Empty, Empty]], rows=2025, cols=3)
        assert actions([[Empty, Empty, Empty], [Empty, Empty, Empty],
                       [Empty, Empty, Yellow]], rows=3, cols=2025)
        assert actions([[Empty, Empty, Empty], [Empty, Empty, Empty],
                       [Empty, Empty, Yellow]], rows=4, cols=3)
        assert actions([[Empty, Empty, Empty], [Empty, Empty, Empty],
                       [Empty, Empty, Yellow]], rows=3, cols=4)
        assert actions([[Empty, Empty, Empty], [Empty, Empty, Empty],
                       [Empty, Empty, Yellow]], rows=4, cols=4)
        assert actions([[Empty, Empty, Empty], [Empty, Empty, Empty], [
                       Empty, Empty, Yellow]], rows=2025, cols=2025)

    with raises(TypeError):
        assert actions(2025, rows=2025, cols=2025)
        assert actions(False, rows=2025, cols=2025)
        assert actions('Alireza', rows=2025, cols=2025)
        assert actions([[Empty, Empty, Empty], [Empty, Empty, Empty], [
                       Empty, Empty, Empty]], rows='Alireza', cols=3)
        assert actions([[Empty, Empty, Empty], [Empty, Empty, Empty],
                       [Empty, Empty, Empty]], rows=False, cols=3)
        assert actions([[Empty, Empty, Empty], [Empty, Empty, Empty], [Empty, Empty, Empty]],
                       rows=[2394, 3234, 4552], cols=3)


def test_result():

    assert result([[Empty, Red, Yellow]], (0, 0), rows=1, cols=3,
                  player_turn=Yellow) == [[Yellow, Red, Yellow]]
    assert result([[Empty, Red, Yellow]], (0, 0), rows=1, cols=3,
                  player_turn=Red) == [[Red, Red, Yellow]]
    assert result([[Empty, Empty, Empty], [Empty, Empty, Empty], [Red, Red, Yellow]], (1, 1), rows=3,
                  cols=3, player_turn=Red) == [[Empty, Empty, Empty], [Empty, Red, Empty], [Red, Red, Yellow]]
    assert result([[Empty, Empty, Empty], [Empty, Empty, Empty], [Red, Red, Yellow]], (1, 1), rows=3,
                  cols=3, player_turn=Yellow) == [[Empty, Empty, Empty], [Empty, Yellow, Empty], [Red, Red, Yellow]]

    with raises(IndexError):
        result([[Empty, Red, Yellow]], (-2025, -2025), rows=1, cols=3, player_turn=Yellow)
        result([[Empty, Red, Yellow]], (0, -2025), rows=1, cols=3, player_turn=Yellow)
        result([[Empty, Red, Yellow]], (-2025,  0), rows=1, cols=3, player_turn=Yellow)

    with raises(NotImplementedError):
        result([[Empty, Red, Yellow]], (0, 1), rows=1, cols=3, player_turn=Yellow)
        result([[Empty, Red, Yellow]], (0, 2), rows=1, cols=3, player_turn=Yellow)
        result([[Red, Red, Yellow]], (0,  0), rows=1, cols=3, player_turn=Yellow)


def test_winner():
    assert winner([[Empty, Empty, Empty]], rows=1, cols=3) == Empty
    assert winner([[Empty, Empty, Empty], [Empty, Red, Yellow],
                  [Red, Red, Red]], rows=3, cols=3) == Empty
    assert winner([[Empty, Empty, Empty, Empty], [Empty, Red, Yellow, Empty],
                  [Red, Red, Red, Red]], rows=3, cols=4) == Red
    assert winner([[Empty, Empty, Empty, Empty], [Empty, Red, Yellow, Empty],
                  [Yellow, Yellow, Yellow, Yellow]], rows=3, cols=4) == Yellow
    assert winner([[Yellow, Empty, Empty, Empty], [Yellow, Empty, Empty, Empty], [
                  Yellow, Empty, Empty, Empty], [Yellow, Red, Red, Red]], rows=4, cols=4) == Yellow
    assert winner([[Red, Empty, Empty, Empty], [Red, Empty, Empty, Empty], [
                  Red, Empty, Empty, Empty], [Red, Yellow, Yellow, Yellow]], rows=4, cols=4) == Red
    assert winner([[Red, Empty, Empty, Empty], [Red, Empty, Empty, Empty], [
                  Red, Empty, Empty, Empty], [Red, Yellow, Yellow, Yellow]], rows=4, cols=4) == Red
    assert winner([[Empty, Empty, Empty, Yellow], [Red, Empty, Yellow, Red], [
                  Empty, Yellow, Red, Red], [Yellow, Red, Red, Red]], rows=4, cols=4) == Yellow


def test_terminal():
    assert terminal([[Empty, Empty, Empty]], rows=1, cols=3) == False
    assert terminal([[Empty, Empty, Empty], [Empty, Red, Yellow],
                     [Red, Red, Red]], rows=3, cols=3) == False
    assert terminal([[Empty, Empty, Empty, Empty], [Empty, Red, Yellow, Empty],
                     [Red, Red, Red, Red]], rows=3, cols=4) == True
    assert terminal([[Empty, Empty, Empty, Empty], [Empty, Red, Yellow, Empty],
                     [Yellow, Yellow, Yellow, Yellow]], rows=3, cols=4) == True
    assert terminal([[Yellow, Empty, Empty, Empty], [Yellow, Empty, Empty, Empty], [
        Yellow, Empty, Empty, Empty], [Yellow, Red, Red, Red]], rows=4, cols=4) == True
    assert terminal([[Red, Empty, Empty, Empty], [Red, Empty, Empty, Empty], [
        Red, Empty, Empty, Empty], [Red, Yellow, Yellow, Yellow]], rows=4, cols=4) == True
    assert terminal([[Red, Empty, Empty, Empty], [Red, Empty, Empty, Empty], [
        Red, Empty, Empty, Empty], [Red, Yellow, Yellow, Yellow]], rows=4, cols=4) == True
    assert terminal([[Empty, Empty, Empty, Yellow], [Red, Empty, Yellow, Red], [
        Empty, Yellow, Red, Red], [Yellow, Red, Red, Red]], rows=4, cols=4) == True
    assert terminal([[Red, Yellow, Red, Yellow], [Red, Yellow, Red, Yellow], [
                    Yellow, Red, Yellow, Red], [Yellow, Red, Yellow, Red]], rows=4, cols=4) == True


def test_utility():
    assert utility([[Red, Yellow, Red, Yellow], [Red, Yellow, Red, Yellow], [
                    Yellow, Red, Yellow, Red], [Yellow, Red, Yellow, Red]], rows=4, cols=4) == 0
    assert utility([[Yellow, Empty, Empty, Empty], [Yellow, Empty, Empty, Empty], [
        Yellow, Empty, Empty, Empty], [Yellow, Red, Red, Red]], rows=4, cols=4) == -1
    assert utility([[Red, Empty, Empty, Empty], [Red, Empty, Empty, Empty], [
        Red, Empty, Empty, Empty], [Red, Yellow, Yellow, Yellow]], rows=4, cols=4) == 1
