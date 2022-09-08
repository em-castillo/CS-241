'''W06 Reading Class Inheritance - Parent and Child Classes'''

# Parent Class


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


# Child Class 1
# With child classes, we can choose to add more methods,
# override existing parent methods, or accept the default
# parent methods with the pass keyword,
class Trout(Fish):
    def __init__(self, water="freshwater"):
        self.water = water
        # you can gain access to inherited methods that have been overwritten in a class object.
        super().__init__(self)
    # pass


# Child Class 2
class Clownfish(Fish):
    # Adds own function live_with_anemone
    def live_with_anemone(self):
        print("The clownfish is coexisting with sea anemone.")


# Child Class 3
class Shark(Fish):
    # overrides __init__ and swim_backwards methods because sharks have different qualities
    def __init__(self, first_name, last_name="Shark",
                 skeleton="cartilage", eyelids=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")


# Creating Trout object or instance
# terry = Trout("Terry")
# print(terry.first_name + " " + terry.last_name)
# print(terry.skeleton)
# print(terry.eyelids)
# terry.swim()
# terry.swim_backwards()
...
# Creating Trout object or instance with super()
terry = Trout()

# Initialize first name
terry.first_name = "Terry"

# Use parent __init__() through super()
print(terry.first_name + " " + terry.last_name)
print(terry.eyelids)

# Use child __init__() override
print(terry.water)

# Use parent swim() method
terry.swim()


# Creating Clownfish object or instance
casey = Clownfish("Casey")
print(casey.first_name + " " + casey.last_name)
casey.swim()
casey.live_with_anemone()

# Creating Shark object or instance
sammy = Shark("Sammy")
print(sammy.first_name + " " + sammy.last_name)
sammy.swim()
sammy.swim_backwards()
print(sammy.eyelids)
print(sammy.skeleton)


'''Multiple inheritance'''

# Parent Class 1


class Coral:
    def community(self):
        print("Coral lives in a community.")


# Parent Class 2
class Anemone:

    def protect_clownfish(self):
        print("The anemone is protecting the clownfish.")


# Child Class
class CoralReef(Coral, Anemone):
    pass


# instantiate a CoralReef object
great_barrier = CoralReef()
great_barrier.community()
great_barrier.protect_clownfish()


# Reading: 45 min
