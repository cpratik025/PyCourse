class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1=Cat('Babli',5)
cat2=Cat('Babl',15)
cat3=Cat('Bab',25)

def maxage(*args):
    return max(*args)

print(f"The oldest cat is x years old {maxage(cat1.age,cat2.age,cat3.age)}")