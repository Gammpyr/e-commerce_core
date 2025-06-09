class MixinLog:
    def __init__(self) -> None:
        print(f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})")
