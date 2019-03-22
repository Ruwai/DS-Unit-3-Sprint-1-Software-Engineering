
import random
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []

    for i in range(num_products):
        name = (random.choice(ADJECTIVES) + " " + random.choice(NOUNS))
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)
        product = Product(name, price, weight, flammability)
        products.append([product.name, product.price,
                         product.weight, product.flammability])

    return products

def inventory_report(products):
    name, price, weight, flammability = zip(*products)

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique Product Names: ', len(set(name)))
    print('Average Price: ', sum(price)/len(price))
    print('Average Weight: ', sum(weight)/len(weight))
    print('Average flammability: ', sum(flammability)/len(flammability))

if __name__ == '__main__':
    inventory_report(generate_products())