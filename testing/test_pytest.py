from python.calc import Calc


class TestCalc:
    def setup(self):
        self.calc = Calc()

    def test_add(self):
        assert self.calc.add(1, 2) == 3

    def test_add2(self):
        assert self.calc.add(1, ) == 4

    def test_add3(self):
        assert self.calc.add() ==

    def test_div(self):
        assert self.calc.div(1, 2) == 0.5

    def test_div2(self):
        assert self.calc.div(1, 0) == EOFError

