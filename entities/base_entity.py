from dataclasses import dataclass

@dataclass
class Tamagochi:
    _name: str = "tamagoch"
    _hp: int = 100
    _hungry: int = 100
    _fatigue: int = 0
    _age: int = 0
    _life_rate: float = 0.1

    @property
    def name(self) -> str:
        return self._name

    @property
    def hp(self) -> int:
        return self._hp
    
    @property
    def hungry(self) -> int:
        return self._hungry
    
    @property
    def fatigue(self) -> int:
        return self._fatigue
    
    @property
    def age(self) -> int:
        return self._age

    @property
    def life_rate(self) -> float:
        return self._life_rate

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp += value
        if self._hp <= 0:
            return "You ar dead"
    
    @hungry.setter
    def hungry(self, value: int) -> None:
        self._hungry += value
    
    @fatigue.setter
    def fatigue(self, value: int) -> None:
        self._fatigue += value

    @age.setter
    def age(self) -> None:
        self._age += 1    

    @life_rate.setter
    def life_rate(self, value: float) -> None:
        self._life_rate += value
