from Clock import Clock
from time import sleep


def main():
    clock = Clock()

    try:
        while True:
            print("\r" + clock.get_time(), end="")
            clock.tick()
            sleep(1)
    except KeyboardInterrupt as e:
        print("\nClock stopped.")


if __name__ == "__main__":
    main()
