class Accumulator(object):
	def __init__(self):
		self.container = []
	def accumulate(self, obj):
		self.container.append(obj)
	def stuff(self):

		return self.container[:]

caja = Accumulator()

caja.accumulate('taza')

print(caja.stuff())

print(caja.stuff().pop()) # sacamos 'la taza'

print(caja.stuff()) # pero la taza sigue ahí


class Fish:
    def __init__(self, first_name, last_name="Fish",
                 skeleton="bone", eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):
        print("The fish is swimming.")

    def swim_backwards(self):
        print("The fish can swim backwards.")


class Trout(Fish):
    def __init__(self, water = "freshwater"):
        self.water = water
        super().__init__(self)


terry = Trout()

# Initialize first name
#terry.first_name = "Terry"

# Use parent __init__() through super()

print(terry.first_name)
#print(terry.eyelids)

# Use child __init__() override
#print(terry.water)

# Use parent swim() method
terry.swim()