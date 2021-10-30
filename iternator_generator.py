#Legacy Iterator

class Iter:
    def __init__(self, max_number):
        self.max_number = max_number

    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        self.current += 1
        if self.current >= self.max_number:
            raise StopIteration("Done")
        return self.current


if __name__ == "__main__":

    x = Iter(15)

    for i in x:
        print(i)


    #New Iterator -> Generator
    def gen():
        yield 1
        yield 2
        yield 3


    for iteration in [1, 2, 3]:
        print(iteration)

    #basic
    listas = [1,2,3,4,5,6,7,8,9,10]
    listas2 = iter(range(1, 11))


    print(next(listas2))
    print(next(listas2))
    print(next(listas2))
    print("Ciklo pradžia")

    for i in listas2:
        print(i)
    #Under the for Loop concept
    while True:
        try:
            print(next(listas2))
        except StopIteration:
            print("Done")
            break


