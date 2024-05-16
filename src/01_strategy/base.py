from abc import abstractmethod, ABC
from typing import Protocol


class FlyBehavior(Protocol):
    def fly(self): ...


class QuackBehavior(Protocol):
    def quack(self): ...


class Duck(ABC):
    def __init__(
        self,
        name: str,
        fly_behavior: type[FlyBehavior],
        quack_behavior: type[QuackBehavior],
    ):
        self._name = name
        self._fly_behavior = fly_behavior()
        self._quack_behavior = quack_behavior()

    def perform_fly(self):
        self._fly_behavior.fly()

    def perform_quack(self):
        self._quack_behavior.quack()

    def swim(self):
        print(self, 'Swim')

    def set_fly_behavior(self, fly_behavior: type[FlyBehavior]):
        self._fly_behavior = fly_behavior()

    def set_quack_behavior(self, quack_behavior: type[QuackBehavior]):
        self._quack_behavior = quack_behavior()

    @abstractmethod
    def display(self):
        raise NotImplementedError
