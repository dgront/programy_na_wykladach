from __future__ import annotations
# --- singleton in Python


class Singleton:
    __instance : Singleton | None = None
    __started = False

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if not self.__started:
            self.__started = True
            print("here")

print("Singleton pattern in Python:")
a = Singleton()
b = Singleton()
print(a, b)
print("a and b objects are the same object:", a is b)   # True




# --- singleton in Python: Thread-safe variant
from threading import Lock


class Singleton:
    __instance = None
    __started = False
    __lock = Lock()

    def __new__(cls):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if not self.__started:
            self.__started = True
            print("here")


print("Singleton pattern - thread-safe version")
a = Singleton()
b = Singleton()

print("a and b objects are the same object:", a is b)   # True

# --- Strategy pattern

from abc import ABC, abstractmethod

class WaysToDoStuff:

    @abstractmethod
    def do_it(self): pass

class BaseStrategy(WaysToDoStuff):
    def do_it(self): print("just something basic")

class FancyStrategy(WaysToDoStuff):
    def do_it(self): print("now something fancy")
class DoesStuff:
    def __init__(self):
        self.__strategy = BaseStrategy()
    def do_your_task(self):
        print("This is how your issue has been handled:")
        self.__strategy.do_it()

    def change_strategy(self, new_strategy):
        self.__strategy = new_strategy

object = DoesStuff()
object.do_your_task()
object.do_your_task()
unusual_condition = True
if unusual_condition:
    object.change_strategy(FancyStrategy())
object.do_your_task()