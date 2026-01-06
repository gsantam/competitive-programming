class DiningPhilosophers:

    def __init__(self):
        self.locks = [threading.Lock() for x in range(5)]
        for i in range(1,5):
            self.locks[i].acquire()


    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        self.locks[philosopher].acquire()
        print(philosopher)
        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()
        self.locks[(philosopher+1)%5].release()
