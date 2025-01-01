from django.test import TestCase
from supermarket.views import CheckoutView

class CheckoutSystemTestCase(TestCase):
    def setUp(self):
        # Initialize the CheckoutSystem instance before each test
        self.checkout = CheckoutView()

    def test_empty_input(self):
        self.assertEqual(self.checkout.calculate_total(""), 0)

    def test_single_items(self):
        self.assertEqual(self.checkout.calculate_total("A"), 50)
        self.assertEqual(self.checkout.calculate_total("B"), 30)
        self.assertEqual(self.checkout.calculate_total("C"), 20)
        self.assertEqual(self.checkout.calculate_total("D"), 15)

    def test_multiple_items_no_discount(self):
        self.assertEqual(self.checkout.calculate_total("AB"), 80)
        self.assertEqual(self.checkout.calculate_total("CD"), 35)
        self.assertEqual(self.checkout.calculate_total("ABC"), 100)
        self.assertEqual(self.checkout.calculate_total("DCB"), 65)

    def test_exact_discount_matches(self):
        self.assertEqual(self.checkout.calculate_total("AAA"), 130)
        self.assertEqual(self.checkout.calculate_total("BB"), 45)

    def test_exceeding_discount_groups(self):
        self.assertEqual(self.checkout.calculate_total("AAAA"), 180)
        self.assertEqual(self.checkout.calculate_total("AAAAAA"), 260)
        self.assertEqual(self.checkout.calculate_total("BBB"), 75)

    def test_mixed_items(self):
        self.assertEqual(self.checkout.calculate_total("AAAB"), 160)
        self.assertEqual(self.checkout.calculate_total("AAABB"), 175)
        self.assertEqual(self.checkout.calculate_total("CDBA"), 115)

    def test_multiple_discounts(self):
        self.assertEqual(self.checkout.calculate_total("BBBB"), 90)
        self.assertEqual(self.checkout.calculate_total("AAABBB"), 205)

    def test_corner_cases(self):
        self.assertEqual(self.checkout.calculate_total("CCCC"), 80)
        self.assertEqual(self.checkout.calculate_total("CCCDD"), 90)
        self.assertEqual(self.checkout.calculate_total("A" * 9), 390)
        self.assertEqual(self.checkout.calculate_total("DABABA"), 190)
        self.assertEqual(self.checkout.calculate_total("A" * 1000), 43340)
        self.assertEqual(self.checkout.calculate_total("ABCD" * 250), 25215)
        self.assertEqual(self.checkout.calculate_total("AAABBBCCDDAEE"), 325)
        self.assertEqual(self.checkout.calculate_total("XYZ"), 0)
        self.assertEqual(self.checkout.calculate_total("EAAA"), 130)
        self.assertEqual(self.checkout.calculate_total("AAAE"), 130)
        self.assertEqual(self.checkout.calculate_total("AAAABBCCDDAE"), 345)


