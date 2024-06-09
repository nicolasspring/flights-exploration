from pathlib import Path


def get_static_test_file(filename: str):
    here = Path(__file__).resolve().parent
    return here / Path("static") / Path(filename)
