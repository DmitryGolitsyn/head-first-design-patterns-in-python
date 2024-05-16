from concrete import MallardDuck, FlyNoWay, Squeak, ModelDuck, FlyRocketPowered


class ShowCase:
    @staticmethod
    def mini_duck_simulator():
        print('Mini Duck Simulator')
        mallard = MallardDuck()
        mallard.display()
        mallard.perform_quack()
        mallard.perform_fly()
        mallard.swim()
        print()
        print('Change behavior:')
        mallard.set_fly_behavior(fly_behavior=FlyNoWay)
        mallard.set_quack_behavior(quack_behavior=Squeak)
        mallard.display()
        mallard.perform_quack()
        mallard.perform_fly()
        mallard.swim()
        print()
        print('Other duck:')
        model = ModelDuck()
        model.display()
        model.perform_quack()
        model.perform_fly()
        model.swim()
        print()
        print('Change behavior:')
        model.set_fly_behavior(fly_behavior=FlyRocketPowered)
        model.set_quack_behavior(quack_behavior=Squeak)
        model.display()
        model.perform_quack()
        model.perform_fly()
        model.swim()
        print('End of Mini Duck Simulator')
        print('-' * 20, '\n' * 3)


if __name__ == '__main__':
    print(
        """
        Strategy Pattern.
        The Strategy Pattern defines a family of algorithms, encapsulates each one, 
        and makes them interchangeable. 
        Strategy lets the algorithm vary independently from clients that use it.
        """
    )
    ShowCase.mini_duck_simulator()
