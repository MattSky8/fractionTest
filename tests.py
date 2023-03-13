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
        self.assertEqual(a.numerator/a.denominator, a.__float__(), msg="test_notWholeNumber failed: "
                                                                       "Fraction(65, 12).__float__() incorrect")

        a = Fraction(-15, 19)
        self.assertEqual(a.numerator / a.denominator, a.__float__(), msg="test_notWholeNumber failed: "
                                                                         "Fraction(-15, 19).__float__() incorrect")

        a = Fraction(1, 7)
        self.assertEqual(a.numerator / a.denominator, a.__float__(), msg="test_notWholeNumber failed: "
                                                                         "Fraction(1, 7).__float__() incorrect")
