from pydantic import BaseModel, validator, ValidationError


class Foo(BaseModel):
    name: str
    bar: int
    baz: int

    def add_one(self):
        self.bar += 1



t = Foo(name="Misha", bar=1, baz=2)
t.add_one()
print(t.bar)
