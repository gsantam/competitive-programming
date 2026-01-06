import threading

class FooBar:
    def __init__(self, n):
        self.n = n
        self.lf = threading.Lock()
        self.lb = threading.Lock()
        self.lb.acquire()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.lf.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.lb.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.lb.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.lf.release()
        self.lb.release()
