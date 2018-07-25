class Fib():
    def __init__(self, n):
        self.n = n
        self.current = 0
        self.num1 = 0
        self.num2 = 2

    def __next__(self):
        if self.current < self.n:
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            self.current = self.current + 1
            return self.num1
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    fib = Fib(10)
    for m in fib:
        print(m)
