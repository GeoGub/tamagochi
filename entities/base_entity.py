class Tamagochi():

    def __init__(self) -> None:
        self._name: str = "tamagoch"
        self._hp: int = 100
        self._hungry: int = 70
        self._fatigue: int = 70 # Усталость
        self._age: int = 0
        self._needs = {
            "e": self._hungry,
            "s": self._fatigue,
        }
        self._image: str = "*****\n ***\n  *  "

    def check_attribute_value(self, attribute, value: int) -> int:
        attribute = value
        if attribute < 0:
            return 0
        elif attribute > 100:
            return 100
        return attribute

    @property
    def needs(self):
        return self._needs

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> int:
        self._hp = self.check_attribute_value(self._hp, value)
        if self._hp == 0:
            raise ValueError

    @property
    def hungry(self) -> int:
        return self._hungry

    @hungry.setter
    def hungry(self, value: int) -> None:
        self._hungry = self.check_attribute_value(self._hungry, value)

    @property
    def fatigue(self) -> int:
        return self._fatigue

    @fatigue.setter
    def fatigue(self, value: int) -> None:
        self._fatigue = self.check_attribute_value(self._fatigue, value)
        if self._fatigue == 100:
            # Вырубать тамагочу от усталости
            pass

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        self._age += value

    @property
    def image(self) -> str:
        return self._image

    def generate_attr_line(self, value: int | float, ratio: int = 10) -> str:
        return "".join(["+" for _ in range(round(value / ratio))])

    def __str__(self) -> str:
        hp_line = self.generate_attr_line(self.hp)
        hungry_line = self.generate_attr_line(self.hungry)
        fatigue_line = self.generate_attr_line(self.fatigue)
        return f"HP: [{hp_line}] {self.hp} | HUNGRY: [{hungry_line}] {self.hungry} | "\
               f"FATIGUE: [{fatigue_line}] {self.fatigue} | AGE: {self.age}"

if __name__ == "__main__":
    tama = Tamagochi()
    print(tama)
    tama.hungry += 10
