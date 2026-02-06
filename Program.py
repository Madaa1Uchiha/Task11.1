from Clock import Clock
from time import sleep


def main():    # this is the run execution of the program 
    clock = Clock(hours=23, minutes=59, seconds=50)
    try:
        while True:
            print("\r" + clock.get_time(), end="")
            clock.tick()
            sleep(1)
    except KeyboardInterrupt as e:
        print("\nClock stopped.")


if __name__ == "__main__":

    main()
