from pytest_demo.calculator import Calculator

def test_add() ->None:
    calc = Calculator()
    assert calc.add(2,1) == 3

def test_div() ->None:
    calc = Calculator()
    assert calc.div(2,1) == 2