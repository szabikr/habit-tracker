import logging
from pathlib import Path
from typing import List

logger = logging.getLogger(__name__)

def read_user_input(filename: str) -> List[str]:
    user_input_dir = "user_input"
    file = Path.cwd().joinpath(user_input_dir, filename)

    try:
        with file.open("r", encoding="utf-8") as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        logger.exception(f"File '{file}' does not exist")
        return []
    return lines

if __name__ == "__main__":
    filename = "user_input_example.txt"
    user_input = read_user_input(filename)
    print(user_input)