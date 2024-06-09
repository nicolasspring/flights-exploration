import argparse
import sys

from flights_exploration import constants as C


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input",
        type=argparse.FileType("r"),
        default=sys.stdin,
        help="the input file to postprocess",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=argparse.FileType("w"),
        default=sys.stdout,
        help="the output file after postprocessing",
    )
    parser.add_argument(
        "-d",
        "--dataset",
        type=str,
        required=True,
        help="specify the type of dataset to read",
    )
    args = parser.parse_args()
    return args


def main(args: argparse.Namespace):
    reader = C.READERS[args.dataset]()
    for flight in reader.iter_flights(args.input):
        print(flight)


if __name__ == "__main__":
    args = parse_args()
    main(args)
