import argparse
import logging
import sys


def init_logging():
    FORMAT = '%(asctime)s - %(message)s'
    # logging.basicConfig(format=FORMAT)
    # logging.basicConfig(level=logging.DEBUG)
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)

def main():
    init_logging()

    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    logging.info('program start')


    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover