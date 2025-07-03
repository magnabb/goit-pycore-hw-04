import os
from typing import Any, Optional, Generator

def file_iterator(path: str) -> Generator[str, Any, Optional[list[Any]]]:
    if not path:
        return []

    if not os.path.isfile(path):
        return []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line
        return None
