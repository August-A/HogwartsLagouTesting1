from python.calc import Calc


class TestCalc:
    def setup(self):
        self.calc = Calc()

    # 加法-有效等价类
    # 1. 两个正数相加
    def test_add(self):
        assert self.calc.add(1, 2) == 3

    # 2. 两个负数相加
    def test_add2(self):
        assert self.calc.add(-1, -2) == -3

    # 3. 一个整数一个负数相加
    def test_add3(self):
        assert self.calc.add(1, -2) == -1

    # 4. 两个小数相加
    def test_add4(self):
        assert self.calc.add(0.11, 0.22) == 0.33

    # 加法-无效等价类
    # 1. 两个正数相加，结果错误
    def test_add5(self):
        assert self.calc.add(1, 2) == 4

    # 2. 两个负数相加，结果错误
    def test_add6(self):
        assert self.calc.add(-1, -2) == -5

    # 除法-有效等价类
    # 1. 两个正数相除，结果为整数
    def test_div(self):
        assert self.calc.div(6, 3) == 2

    # 2. 两个正数相除，结果为小数
    def test_div2(self):
        assert self.calc.div(3, 6) == 0.5

    # 3. 正数除以负数
    def test_div3(self):
        assert self.calc.div(-6, 3) == -2

    # 4. 两个负数相除
    def test_div4(self):
        assert self.calc.div(-6, -3) == 2

    # 5. 0除以一个数，结果为0
    def test_div5(self):
        assert self.calc.div(0, 100) == 0

    # 6. 两个小数相除
    def test_div6(self):
        assert self.calc.div(2.48, 1.24) == 2

    # 除法-无效等价类
    # 1. 除数为零，报错
    def test_div7(self):
        assert self.calc.div(1, 0) == 0

    # 2. 两正数相除，结果错误
    def test_div8(self):
        assert self.calc.div(6, 3) == 3

    # 3. 正数除以负数，结果错误
    def test_div9(self):
        assert self.calc.div(6, -3) == 2
