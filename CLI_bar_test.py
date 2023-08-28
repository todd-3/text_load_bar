import argparse
from loading_bar import LoadingBar
from sys import argv
from random import randint
from time import sleep

def parse_args(args_in) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="CLI interface for LoadBar class, created for easier testing")
    parser.add_argument("-p", dest="prefix", type=str, default="Loading")
    parser.add_argument("-l", dest="length", type=int, default=30)
    parser.add_argument("-t", dest="total", type=int, default=randint(100, 500))
    parser.add_argument("-a", dest="auto_size", action="store_true")

    return parser.parse_args(args_in)

if __name__ == "__main__":
    args = parse_args(argv[1:])
    args_convert = vars(args)  # converts Namespace object to dict
    bar = LoadingBar(**args_convert)

    print(f"Total was set to ", args.total)
    for i in range(args.total):
        bar()
        sleep(0.1)
