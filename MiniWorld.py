class Sun:
    light = True
    air = 20
    
    @classmethod
    def set_light(cls, state):
        cls.light = state
    
    @classmethod
    def info(cls):
        print(f"IN OUR WORLD WE HAVE {cls.air} OXYGEN\n")

class Moon:
    light = False

    @classmethod
    def set_light(cls, state):
        cls.light = state

class Grass:
    growth = 1.0   

    def to_grow(self):
        if Sun.light:
            Grass.growth += 1.0
            print(f"Grass is growing when it's day.\n")
        elif Moon.light:
            print(f"Grass isn't growing at night.\n")
    
    def height_of_grass(self):
        print(f"The height of grass is - {Grass.growth}cm\n")

class Tree:
    height = 2

    def growing(self):
        if Sun.light:
            Tree.height += 0.1
            print(f"Tree is growing when it's day.\n")
        elif Moon.light:
            print(f"Tree isn't growing at night.\n")
    
    def height_of_tree(self):
        print(f"The height of tree - {Tree.height}m\n")    
    
    def photosynthesis(self):
        print("Trees produce oxygen\n")
        if Sun.light:
            Sun.air += 2
            print(f"Now we have {Sun.air} oxygen!\n")
        elif Moon.light:
            print("But can't do it at night!\n")

class Shep:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def go_ahead(self):
        if Sun.light:
            print("^\n")
            self.y += 1
            return self.y 
        elif Moon.light:
            print("zzzzzz!\n")
    
    def go_back(self):
        if Sun.light:
            print("back)\n")
            self.y -= 1
            return self.y 
        elif Moon.light:
            print("zzzzzz!\n")
    
    def go_left(self):
        if Sun.light:
            print("<-\n")
            self.x -= 1
            return self.x
        elif Moon.light:
            print("zzzzzz!\n")
    
    def go_right(self):
        if Sun.light:
            print("->\n")
            self.x += 1
            return self.x
        elif Moon.light:
            print("zzzzzz!\n")
    
    def location_of_the_sheep(self):
        print(f"Coordinates of the sheep ({self.x};{self.y})\n")

    def eating_grass(self):
        print("Shep likes grass!\n")
        if Sun.light:
            Grass.growth -= 0.1
            return Grass.growth
        elif Moon.light:
            print("But at night he prefers sleeping!\n")

class Controller:
    def __init__(self, sun, moon, grass, tree, sheep):
        self.sun = sun
        self.moon = moon
        self.grass = grass
        self.tree = tree
        self.sheep = sheep
    
    def switch_to_day(self):
        Sun.set_light(True)
        Moon.set_light(False)
        print("It's now day.\n")
        Sun.info()

    def switch_to_night(self):
        Sun.set_light(False)
        Moon.set_light(True)
        print("It's now night.\n")
    
    def make_day(self):
        self.switch_to_day()

        self.grass.to_grow()
        self.grass.height_of_grass()
        self.tree.growing()
        self.tree.height_of_tree()
        self.tree.photosynthesis()
        Sun.info()
        self.sheep.location_of_the_sheep()
        self.sheep.go_ahead()
        self.sheep.go_left()
        self.sheep.go_left()
        self.sheep.go_left()
        self.sheep.go_ahead()
        self.sheep.go_ahead()
        self.sheep.go_right()
        self.sheep.go_back()
        self.sheep.location_of_the_sheep()
        self.sheep.eating_grass()
        self.grass.height_of_grass()

        self.switch_to_night()
        self.grass.to_grow()
        self.grass.height_of_grass()
        self.tree.growing()
        self.tree.height_of_tree()
        self.sheep.eating_grass()
        self.sheep.go_left()
        self.sheep.go_right()

sun = Sun()
moon = Moon()
grass = Grass()
tree = Tree()
sheep = Shep(0, 0)

controller = Controller(sun, moon, grass, tree, sheep)
controller.make_day()
