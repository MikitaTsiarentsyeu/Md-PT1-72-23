class Engine:

    def __init__(self, power, volume):
        self.power = power
        self.volume = volume

    def __set_power(self, power):
        self.__power = power

    def get_power(self):
        return self.__power

    def __set_volume(self, volume):
        self.__volume = volume

    def get_volume(self):
        return self.__volume

    power = property(get_power, __set_power)
    volume = property(get_volume, __set_volume)

class SerialCar:

    __DEFAULT_COLOR = 'orange'

    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine
        self.color = SerialCar.__DEFAULT_COLOR

    def __set_make(self, make):
        self.__make = make

    def get_make(self):
        return self.__make
    
    def __set_model(self, model):
        self.__model = model

    def get_model(self):
        return self.__model
    
    def get_default_color(self):
        return SerialCar.__DEFAULT_COLOR

    make = property(get_make, __set_make)
    model = property(get_model, __set_model)
    default_color = property(get_default_color)

v4 = Engine(112, 1.2)
polo = SerialCar("vw", "polo", v4)


print(polo.default_color)
print(polo.default_color == polo.color)

polo.color = "green"
print(polo.default_color == polo.color)

print(polo.engine.volume)

polo.engine = Engine(220, 4)

print(polo.engine.volume)

class SuperCar:

    __DEFAULT_POWER = 330   
    __DEFAULT_VOLUME = 8

    class __Engine:

        def __init__(self, power, volume):
            self.power = power
            self.volume = volume

        def __set_power(self, power):
            self.__power = power

        def get_power(self):
            return self.__power

        def __set_volume(self, volume):
            self.__volume = volume

        def get_volume(self):
            return self.__volume

        power = property(get_power, __set_power)
        volume = property(get_volume, __set_volume)

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.__engine = SuperCar.__Engine(SuperCar.__DEFAULT_POWER, SuperCar.__DEFAULT_VOLUME)

    def __set_make(self, make):
        self.__make = make

    def get_make(self):
        return self.__make
    
    def __set_model(self, model):
        self.__model = model

    def get_model(self):
        return self.__model
    
    def get_power(self):
        return self.__engine.power
    
    def get_volume(self):
        return self.__engine.volume
    
    make = property(get_make, __set_make)
    model = property(get_model, __set_model)
    power = property(get_power)
    volume = property(get_volume)

sc = SuperCar("ferrari", "la ferrari")
print(sc.power)