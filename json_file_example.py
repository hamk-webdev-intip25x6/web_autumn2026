"""Read and write dictionaries as UTF-8 encoded JSON files."""

import json
import os
from typing import Any, Optional


def load_dictionary(path: os.PathLike[str] | str) -> Optional[dict[str, Any]]:
    """Load a dictionary from a UTF-8 encoded JSON file.

    Args:
        path: The file path to read.

    Returns:
        The dictionary stored in the file, or ``None`` if the file cannot be
        read, parsed, or does not contain a dictionary.
    """
    try:
        if not isinstance(path, (str, os.PathLike)):
            raise TypeError("path must be a string or path-like object")

        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError("the JSON document must contain a dictionary")

        return data
    except FileNotFoundError:
        print(f"Error: file '{path}' was not found.")
    except IsADirectoryError:
        print(f"Error: '{path}' is a directory, not a JSON file.")
    except PermissionError:
        print(f"Error: permission denied while reading '{path}'.")
    except UnicodeDecodeError:
        print(f"Error: '{path}' is not valid UTF-8 text.")
    except json.JSONDecodeError as error:
        print(f"Error: '{path}' contains invalid JSON: {error.msg}.")
    except TypeError as error:
        print(f"Error: invalid path for dictionary loading: {error}.")
    except ValueError as error:
        print(f"Error: invalid dictionary data in '{path}': {error}.")
    except OSError as error:
        print(f"Error: could not read '{path}': {error}.")
    except RecursionError:
        print(f"Error: '{path}' contains JSON data nested too deeply.")
    return None


def save_dictionary(path: os.PathLike[str] | str, d: dict[str, Any]) -> bool:
    """Save a dictionary as a UTF-8 encoded JSON file.

    Args:
        path: The file path to write. An existing file is replaced.
        d: The dictionary to serialize.

    Returns:
        ``True`` if the dictionary was saved; otherwise ``False``.
    """
    try:
        if not isinstance(path, (str, os.PathLike)):
            raise TypeError("path must be a string or path-like object")
        if not isinstance(d, dict):
            raise TypeError("d must be a dictionary")

        serialized = json.dumps(d, ensure_ascii=False, indent=2, allow_nan=False)
        with open(path, "w", encoding="utf-8") as file:
            file.write(serialized)
            file.write("\n")
        return True
    except FileNotFoundError:
        print(f"Error: parent directory for '{path}' was not found.")
    except IsADirectoryError:
        print(f"Error: '{path}' is a directory, not a JSON file.")
    except PermissionError:
        print(f"Error: permission denied while writing '{path}'.")
    except UnicodeEncodeError:
        print(
            f"Error: dictionary contains text that cannot be encoded as UTF-8 "
            f"for '{path}'."
        )
    except TypeError as error:
        if not isinstance(path, (str, os.PathLike)):
            print(f"Error: invalid path for dictionary saving: {error}.")
        else:
            print(f"Error: dictionary cannot be serialized: {error}.")
    except ValueError as error:
        print(f"Error: dictionary contains a value that is not valid JSON: {error}.")
    except OSError as error:
        print(f"Error: could not write '{path}': {error}.")
    except RecursionError:
        print("Error: dictionary is nested too deeply to serialize.")
    return False
