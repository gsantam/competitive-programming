from threading import Lock

class Foo:
    def __init__(self):
        self.ls = Lock()
        self.lt = Lock()
        self.lt.acquire()
        self.ls.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.ls.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.ls.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.lt.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.lt.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.lt.release()
