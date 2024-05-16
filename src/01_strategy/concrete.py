from base import Duck, FlyBehavior, QuackBehavior


class FlyWithWings(FlyBehavior):
    def fly(self):
        print(self, 'I am flying with wings!')


class FlyNoWay(FlyBehavior):
    def fly(self):
        print(self, 'I can not fly!')


class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print(self, 'I am flying with a rocket!')


class Quack(QuackBehavior):
    def quack(self):
        print(self, 'Quack')


class Squeak(QuackBehavior):
    def quack(self):
        print(self, 'Squeak')


class MuteQuack(QuackBehavior):
    def quack(self):
        print(self, '<< Silence >>')


class MallardDuck(Duck):
    def __init__(self):
        super().__init__(
            name='MallardDuck', fly_behavior=FlyWithWings, quack_behavior=Quack
        )

    def display(self):
        print(f'I am {self._name} of {self.__class__.__name__=}')


class ModelDuck(Duck):
    def __init__(self):
        super().__init__(
            name='ModelDuck', fly_behavior=FlyNoWay, quack_behavior=MuteQuack
        )

    def display(self):
        print(f'I am {self._name} of {self.__class__.__name__=}')
