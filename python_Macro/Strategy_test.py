from abc import ABC, abstractmethod

class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def do_operation(self, a, b):
        return self._strategy.execute(a, b)

class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self, a, b):
        return a + b

class ConcreteStrategyB(Strategy):
    def execute(self, a, b):
        return a - b

if __name__ == "__main__":
    context = Context(ConcreteStrategyA())
    print("10 + 5 =", context.do_operation(10, 5))
    context.set_strategy(ConcreteStrategyB())
    print("10 - 5 =", context.do_operation(10, 5))
