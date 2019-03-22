import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_flammability(self):
        prod_a = Product('Test Product', flammability=51, weight=1)
        self.assertEqual(prod_a.explode(), '...BABOOM!!!')
        prod_b = Product('Test Proudct', flammability=9, weight=1)
        self.assertEqual(prod_b.explode(), '...fizzle.')
        prod_c = Product('Test Product', flammability=10, weight=1)
        self.assertEqual(prod_c.explode(), '...boom!')

    def test_default_stealability(self):
        prod_a = Product('Test Product', price=9, weight=20)
        self.assertEqual(prod_a.stealability(), 'Not so stealable...')
        prod_b = Product('Test Product', price=10, weight=20)
        self.assertEqual(prod_b.stealability(), 'Kinda stealable')
        prod_c = Product('Test Product', price=11, weight=10)
        self.assertEqual(prod_c.stealability(), 'Very Stealable!')

class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        products = generate_products()
        self.assertEqual(len(products),30)

    def test_legal_names(self):
        products = generate_products()
        names,prices,weights,flammability = zip(*products)
        accepted_words = ADJECTIVES+NOUNS
        for name in names:
            words = name.split()
            for word in words:
                self.assertIn(word,accepted_words)

if __name__ == '__main__':
    unittest.main()