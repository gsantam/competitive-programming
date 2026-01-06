import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.even_l = threading.Lock()
        self.odd_l = threading.Lock()
        self.even_l.acquire()
        self.odd_l.acquire()
        self.main_l = threading.Lock()
        self.main_l.acquire()

        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.i = i+1
            printNumber(0)
            if self.i%2==0:
                self.even_l.release()
            else:
                self.odd_l.release()
            self.main_l.acquire()
        self.i = -1
        self.even_l.release()
        self.odd_l.release()
        self.main_l.release()


        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            self.even_l.acquire()
            if self.i == -1:
                break
            printNumber(self.i)
            self.main_l.release()

        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            self.odd_l.acquire()
            if self.i == -1:
                break
            printNumber(self.i)
            self.main_l.release()

