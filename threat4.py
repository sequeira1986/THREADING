import time
from concurrent.futures import ThreadPoolExecutor
from threading import Lock


class ShoppingCart:
    def __init__(self):
        self.items = 0
        self.lock = Lock()

    def update(self, name):
        with self.lock:  # Locking the critical section
            print(f'Zákazník-{name}: začína nakupovať')
            local_cart = self.items
            local_cart += 1
            time.sleep(1)  # This sleep simulates some processing time
            self.items = local_cart
            print(f'Zákazník-{name}: nakúpil')


print('Nakupovanie začína')
shopping_cart = ShoppingCart()
print(f'Veľkosť košíka je: {shopping_cart.items}')
with ThreadPoolExecutor(max_workers=3) as executor:
    # Passing the index of the iterable to the update function as the name
    executor.map(shopping_cart.update, range(3))

print(f'Veľkosť košíka po nakupovaní je: {shopping_cart.items}')
