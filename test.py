class Test:
    def __init__(self) -> None:
        self.val = 10
        self.a = {
            "val": self.val
        }

t = Test()
t.a["val"] += 200
print(t.val)
print(t.a["val"])
