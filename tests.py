from fraction import Fraction
import unittest


class TestInit(unittest.TestCase):
    # several of these will need to check to see if an exception is raised
    def test_divZero(self):
        with self.assertRaises(ZeroDivisionError, msg="Denominator of zero fails to raise DivByZero"):
            a = Fraction(1, 0)

    def test_default(self):
        # will the 0 argument version of the constructor produce the correct fraction?
        a = Fraction()
        self.assertEqual(a.numerator, 0, msg="test_default failed: Fraction() does not initialize numerator to 0")
        self.assertEqual(a.denominator, 1, msg="test_default failed: Fraction() does not initialize denominator to 1")

    def test_oneArg(self):
        # will the 1 argument version of the constructor produce the correct fraction?
        a = Fraction(7)
        self.assertEqual(a.numerator, 7, msg="test_oneArg failed: Fraction(7) does not set numerator to 7")
        self.assertEqual(a.denominator, 1, msg="test_oneArg failed: Fraction(7) does not set denominator to 1")

        b = Fraction(-10)
        self.assertEqual(b.numerator, -10, msg="test_oneArg failed: Fraction(-10) does not set numerator to -10")
        self.assertEqual(b.denominator, 1, msg="test_oneArg failed: Fraction(-10) does not set denominator to 1")

        c = Fraction(0)
        self.assertEqual(c.numerator, 0, msg="test_oneArg failed: Fraction(0) does not set numerator to 0")
        self.assertEqual(c.denominator, 1, msg="test_oneArg failed: Fraction(0) does not set denominator to 1")

    def test_twoArg(self):
        # will the 2 argument version of the constructor produce the correct fraction?
        a = Fraction(3, 1)
        self.assertEqual(a.numerator, 3, msg="test_twoArg failed: Fraction(3, 1) does not set numerator to 3")

        b = Fraction(10, 7)
        self.assertEqual(b.numerator, 10, msg="test_twoArg failed: Fraction(10, 7) does not set numerator to 10")
        self.assertEqual(b.denominator, 7, msg="test_twoArg failed: Fraction(10, 7) does not set denominator to 7")

        c = Fraction(-6, 5)
        self.assertEqual(c.numerator, -6, msg="test_twoArg failed: Fraction(-6, 5) does not set numerator to -6")
        self.assertEqual(c.denominator, 5, msg="test_twoArg failed: Fraction(-6, 5) does not set denominator to 5")

        d = Fraction(-2, 3)
        self.assertEqual(d.numerator, -2, msg="test_twoArg failed: Fraction(-2, 3) does not set numerator to -2")
        self.assertEqual(d.denominator, 3, msg="test_twoArg failed: Fraction(-2, 3) does not set denominator to 3")

        e = Fraction(16, -3)
        self.assertEqual(e.numerator, -16, msg="test_twoArg failed: Fraction(16, -3) does not set numerator to -16")
        self.assertEqual(e.denominator, 3, msg="test_twoArg failed: Fraction(16, -3) does not set denominator to 3")

        f = Fraction(-1, -2)
        self.assertEqual(f.numerator, 1, msg="test_twoArg failed: Fraction(-1, -2) does not set numerator to 1")
        self.assertEqual(f.denominator, 2, msg="test_twoArg failed: Fraction(-1, -2) does not set denominator to 2")

    def test_invalidArg(self):
        # will constructor through an exception if non-numeric data is passed?
        with self.assertRaises(TypeError, msg="Numerator = 1.0 does not raise TypeError"):
            a = Fraction(1.0)
        with self.assertRaises(TypeError, msg="Numerator = {1, 2} does not raise TypeError"):
            a = Fraction({1, 2})
        with self.assertRaises(TypeError, msg="Numerator = 1j does not raise TypeError"):
            a = Fraction(1j)
        with self.assertRaises(TypeError, msg="Numerator = Fraction(0,1) does not raise TypeError"):
            a = Fraction(Fraction(0, 1))

        with self.assertRaises(TypeError, msg="Denominator = 1.0 does not raise TypeError"):
            a = Fraction(1, 1.0)
        with self.assertRaises(TypeError, msg="Denominator = {1, 2} does not raise TypeError"):
            a = Fraction(4, {1, 2})
        with self.assertRaises(TypeError, msg="Denominator = 1j does not raise TypeError"):
            a = Fraction(-5, 1j)
        with self.assertRaises(TypeError, msg="Denominator = Fraction(0,1) does not raise TypeError"):
            a = Fraction(-1, Fraction(0, 1))

    def test_reduced(self):
        # if the inputs share a factor, is the fraction reduced? i.e. 2/4 = 1/2
        a = Fraction(2, 2)
        self.assertEqual(a.numerator, 1, "test_reduced failed: Fraction(2,2) does not set numerator to 1")
        self.assertEqual(a.denominator, 1, "test_reduced failed: Fraction(2,2) does not set denominator to 1")

        b = Fraction(33, 6)
        self.assertEqual(b.numerator, 11, "test_reduced failed: Fraction(33, 6) does not set numerator to 11")
        self.assertEqual(b.denominator, 2, "test_reduced failed: Fraction(33, 6) does not set denominator to 2")

        c = Fraction(18, 30)
        self.assertEqual(c.numerator, 3, "test_reduced failed: Fraction(18, 30) does not set numerator to 3")
        self.assertEqual(c.denominator, 5, "test_reduced failed: Fraction(18, 30) does not set denominator to 5")

        d = Fraction(0, 5)
        self.assertEqual(d.numerator, 0, "test_reduced failed: Fraction(0, 5) does not set numerator to 0")
        self.assertEqual(d.denominator, 1, "test_reduced failed: Fraction(0, 5) does not reduce denominator to 1")

        e = Fraction(0, -1)
        self.assertEqual(e.numerator, 0, "test_reduced failed: Fraction(0, -1) does not set numerator to 0")
        self.assertEqual(e.denominator, 1, "test_reduced failed: Fraction(0, -1) does not denominator to 1")

        f = Fraction(0, -10)
        self.assertEqual(f.numerator, 0, "test_reduced failed: Fraction(0, -10) does not set numerator to 0")
        self.assertEqual(f.denominator, 1, "test_reduced failed: Fraction(0, -10) does not reduce denominator to 1")

        g = Fraction(-12, 6)
        self.assertEqual(g.numerator, -2, "test_reduced failed: Fraction(-12, 6) does not reduce numerator to -2")
        self.assertEqual(g.denominator, 1, "test_reduced failed: Fraction(-12, 6) does not reduce denominator to 1")

        h = Fraction(49, -21)
        self.assertEqual(h.numerator, -7, "test_reduced failed: Fraction(49, -21) does not reduce numerator to -7")
        self.assertEqual(h.denominator, 3, "test_reduced failed: Fraction(49, -21) does not reduce denominator to 3")


class TestStr(unittest.TestCase):
    def test_displayfraction(self):
        a = Fraction(1, 2)
        self.assertEqual(" 1/2 ", a.__str__())

    def test_displayInt(self):
        # if the denominator is 1, does display omit the /1?
        a = Fraction(5)
        self.assertEqual("5", a.__str__(), msg="test_displayInt failed: Fraction(5).__str__() is incorrect")

        b = Fraction()
        self.assertEqual("0", b.__str__(), msg="test_displayInt failed: Fraction().__str__() is incorrect")

        c = Fraction(-3, 1)
        self.assertEqual("-3", c.__str__(), msg="test_displayInt failed: Fraction(-3, 1).__str__() is incorrect")

    def test_displayNeg(self):
        # if the fraction is negative, is it possible to erroneously have it display 1/-2, vs -1/2?
        a = Fraction(-1, 2)
        self.assertEqual("-1/2", a.__str__(), msg="test_displayNeg failed: Fraction(-1, 2).__str__() is incorrect")

        b = Fraction(5, -3)
        self.assertEqual("-5/3", b.__str__(), msg="test_displayNeg failed: Fraction(5, -3).__str__() is incorrect")


class TestFloat(unittest.TestCase):
    def test_wholeNumber(self):
        a = Fraction()
        self.assertEqual(0.0, a.__float__(), msg="test_wholeNumber failed: Fraction().__float__() != 0.0")

        b = Fraction(105)
        self.assertEqual(105.0, b.__float__(), msg="test_wholeNumber failed: Fraction(105).__float__() != 105.0")

        c = Fraction(-431)
        self.assertEqual(-431.0, c.__float__(), msg="test_wholeNumber failed: Fraction(-431).__float__() != -431.0")

    def test_notWholeNumber(self):
        a = Fraction(65, 12)
        self.assertEqual(a.numerator / a.denominator, a.__float__(), msg="test_notWholeNumber failed: "
                                                                         "Fraction(65, 12).__float__() incorrect")

        a = Fraction(-15, 19)
        self.assertEqual(a.numerator / a.denominator, a.__float__(), msg="test_notWholeNumber failed: "
                                                                         "Fraction(-15, 19).__float__() incorrect")

        a = Fraction(1, 7)
        self.assertEqual(a.numerator / a.denominator, a.__float__(), msg="test_notWholeNumber failed: "
                                                                         "Fraction(1, 7).__float__() incorrect")


class TestAdd(unittest.TestCase):
    def setUp(self):
        self.zero = Fraction()
        self.a = Fraction(3, 4)
        self.inv_a = Fraction(-3, 4)
        self.b = Fraction(1, 12)
        self.inv_b = Fraction(-1, 12)
        self.c = Fraction(5)
        self.d = Fraction(11, 5)

    def test_addZero(self):
        u = self.a.__add__(self.zero)
        self.assertEqual(u.__str__(), self.a.__str__(), msg="test_addZero failed: 3/4 + 0 != 3/4")

        v = self.inv_b.__add__(self.zero)
        self.assertEqual(v.__str__(), self.inv_b.__str__(), msg="test_addZero failed: -1/12 + 0 != -1/12")

        w = self.zero.__add__(self.zero)
        self.assertEqual(w.__str__(), self.zero.__str__(), msg="test_addZero failed: 0 + 0 != 0")

    def test_addInverse(self):
        u = self.a.__add__(self.inv_a)
        self.assertEqual(u.__str__(), self.zero.__str__(), msg="test_addInverse failed: 3/4 + -3/4 != 0")

        v = self.b.__add__(self.inv_b)
        self.assertEqual(v.__str__(), self.zero.__str__(), msg="test_addInverse failed: 1/12 + -1/12 != 0")

    def test_addGeneral(self):
        u = self.a.__add__(self.b)
        self.assertEqual(u.__str__(), "5/6", msg="test_addGeneral failed: 3/4 + 1/12 != 5/6")

        v = self.a.__add__(self.inv_b)
        self.assertEqual(v.__str__(), "2/3", msg="test_addGeneral failed: 3/4 + -1/12 != 2/3")

        w = self.inv_a.__add__(self.b)
        self.assertEqual(w.__str__(), "-2/3", msg="test_addGeneral failed: -3/4 + 1/12 != -2/3")

        x = self.inv_a.__add__(self.inv_b)
        self.assertEqual(x.__str__(), "-5/6", msg="test_addGeneral failed: -3/4 + -1/12 != -5/6")

        y = self.a.__add__(self.c)
        self.assertEqual(y.__str__(), "23/4", msg="test_addGeneral failed: 3/4 + 5 != 23/4")

        z = self.c.__add__(self.inv_b)
        self.assertEqual(z.__str__(), "59/12", msg="test_addGeneral failed: 5 + -1/12 != 59/12")

        t = self.d.__add__(self.inv_a)
        self.assertEqual(t.__str__(), "29/20", msg="test_addGeneral failed: 11/5 + -3/4 != 29/20")


class TestSub(unittest.TestCase):
    def setUp(self):
        self.zero = Fraction()
        self.a = Fraction(3, 4)
        self.inv_a = Fraction(-3, 4)
        self.b = Fraction(1, 12)
        self.inv_b = Fraction(-1, 12)
        self.c = Fraction(5)
        self.d = Fraction(11, 5)

    def test_subZero(self):
        u = self.a.__sub__(self.zero)
        self.assertEqual(u.__str__(), self.a.__str__(), msg="test_subZero failed: 3/4 - 0 != 3/4")

        v = self.zero.__sub__(self.b)
        self.assertEqual(v.__str__(), self.inv_b.__str__(), msg="test_subZero failed: 0 - 1/12 != -1/12")

        w = self.zero.__sub__(self.zero)
        self.assertEqual(w.__str__(), self.zero.__str__(), msg="test_subZero failed: 0 - 0 != 0")

    def test_subSelf(self):
        u = self.a.__sub__(self.a)
        self.assertEqual(u.__str__(), self.zero.__str__(), msg="test_subSelf failed: 3/4 - 3/4 != 0")

        v = self.inv_b.__sub__(self.inv_b)
        self.assertEqual(v.__str__(), self.zero.__str__(), msg="test_subSelf failed: -1/12 - -1/12 != 0")

    def test_subGeneral(self):
        u = self.a.__sub__(self.inv_b)
        self.assertEqual(u.__str__(), "5/6", msg="test_subGeneral failed: 3/4 - -1/12 != 5/6")

        v = self.a.__sub__(self.b)
        self.assertEqual(v.__str__(), "2/3", msg="test_subGeneral failed: 3/4 - 1/12 != 2/3")

        w = self.inv_a.__sub__(self.inv_b)
        self.assertEqual(w.__str__(), "-2/3", msg="test_subGeneral failed: -3/4 - -1/12 != -2/3")

        x = self.inv_a.__sub__(self.b)
        self.assertEqual(x.__str__(), "-5/6", msg="test_subGeneral failed: -3/4 - 1/12 != -5/6")

        y = self.a.__sub__(self.c)
        self.assertEqual(y.__str__(), "-17/4", msg="test_subGeneral failed: 3/4 - 5 != -17/4")

        z = self.c.__sub__(self.b)
        self.assertEqual(z.__str__(), "59/12", msg="test_subGeneral failed: 5 - 1/12 != 59/12")

        t = self.d.__sub__(self.a)
        self.assertEqual(t.__str__(), "29/20", msg="test_subGeneral failed: 11/5 - 3/4 != 29/20")
