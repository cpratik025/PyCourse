import modules.utility
#import modules.more_shopping.shopping
from modules.more_shopping.shopping import buy
x = modules.utility.multiply(4,2)

print(x)
#cart = modules.more_shopping.shopping.buy('Pencil')
cart = buy('Pencil')
print(cart)