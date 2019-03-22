import random

class Product:
    def __init__(self,name:str,price=int(10),weight=int(20),flammability=float(0.5)):

        try:
            err = 'Product must have a name.'
            assert (name is not None), err
            err = 'Product must have weight.'
            assert (weight is not None), err
            err = "Product must have price."
            assert (price is not None), err
            err = "Product must be flammable."
            assert (flammability is not None), err
            self.name = name
            self.price = price
            self.weight = weight
            self.flammability = flammability
            self.identifier = random.randint(1000000, 9999999)

            return

        except:
            print(err+"Please add a valid value.")

    def stealability(self):
        prob_steal = self.price / self.weight
        if prob_steal < 0.5:
            return 'Not so stealable...'
        else:
            if prob_steal > 1:
                return 'Very Stealable!'
            else:
                return 'Kinda stealable'

    def explode(self):
        explodability = self.flammability * self.weight
        if explodability < 10:
            return '...fizzle.'
        else:
            if explodability > 50:
                return '...BABOOM!!!'
            else:
                return "...boom! :)"

class BoxingGlove(Product):
    def __init__(self,
                 name: str,
                 price=int(10),
                 weight=int(10),
                 flammability=float(0.5)):
        Product.__init__(self, name, price, weight, flammability)
        return

    def explode(self):
        return "...it's a glove"

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        else:
            if self.weight > 15:
                return "OUCH!"
            else:
                return "Hey that hurt!"
