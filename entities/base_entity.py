from pydantic import BaseModel


class Tamagochi(BaseModel):
    name: str = "tamagoch"
    hp: int = 100
    hungry: int = 100
    fatigue: int = 0
    age: int = 0
    life_rate: float = 0.1
    image: str = "*****\n ***\n  *  "

    def update_hp(self, value: int) -> None:
        self.hp += value
        if self.hp <= 0:
            return "You ar dead"
    
    def update_hungry(self, value: int) -> None:
        self.hungry += value
    
    def update_fatigue(self, value: int) -> None:
        self.fatigue += value

    def update_age(self) -> None:
        self.age += 1
        self.life_rate = self.life_rate * self.age + self.life_rate

    def update_life_rate(self, value: float) -> None:
        self.life_rate += value

    def generate_attr_line(self, value: int | float, ratio: int = 10):
        return "".join(["+" for _ in range(round(value / ratio))])

    def __str__(self) -> str:
        hp_line = self.generate_attr_line(self.hp)
        hungry_line = self.generate_attr_line(self.hungry)
        fatigue_line = self.generate_attr_line(self.fatigue)
        return f"HP: [{hp_line}] {self.hp} | HUNGRY: [{hungry_line}] {self.hungry} | FATIGUE: [{fatigue_line}] {self.fatigue} | AGE: {self.age}"

if __name__ == "__main__":
    tama = Tamagochi()
    print(tama)
