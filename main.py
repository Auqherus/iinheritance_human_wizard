class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage


class Archer(Hero):
    def __init__(self, name, health, num_arrows):
        super().__init__(name, health)
        self.__num_arrows = num_arrows
    
    def get_num_arrows(self):
        return self.__num_arrows
    
    def shoot(self, target):
        if self.__num_arrows <= 0:
            raise Exception("not enough arrows")
        self.__num_arrows -= 1
        target.take_damage(10)


class Wizard(Hero):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.__mana = mana

    def get_mana(self):
        return self.__mana

    def cast(self, target):
        #print(f"mana: {self.__mana}")
        if self.__mana < 25:
            raise Exception("not enough mana")
        self.__mana -= 25
        target.take_damage(25)
        #print(f"mana after cast: {self.__mana}")

def main():

    hero_1 = Hero("Astarion", 175)
    archer_1 = Archer("Shadowhearth", 125, 12)
    wizard_1 = Wizard("Auqherus", 155, 250)
    print(f"Hero's name: {hero_1.get_name()}")
    print(f"Hero's health: {hero_1.get_health()}\n")

    print(f"Archers's name: {archer_1.get_name()}")
    print(f"Archers's health: {archer_1.get_health()}")
    print(f"Archers's number of arrows: {archer_1.get_num_arrows()}\n")

    print(f"Wizard's name: {wizard_1.get_name()}")
    print(f"Wizard's health: {wizard_1.get_health()}")
    print(f"Wizard's mana: {wizard_1.get_mana()}")


main()
