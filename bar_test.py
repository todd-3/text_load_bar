from loading_bar import LoadingBar
from random import randint
from time import sleep

if __name__ == "__main__":
    l = randint(20, 500)
    print(l)

    t = LoadingBar(total=l, prefix="loading", length=30)

    for i in range(l):
        t(1)
        sleep(0.2)

    print("done")
