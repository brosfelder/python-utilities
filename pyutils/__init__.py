"""Python Utilities Package - Collection of utility functions."""

__version__ = "0.1.0"

from pyutils.string_utils import slugify, truncate, camel_to_snake
from pyutils.list_utils import chunk_list, flatten_list, remove_duplicates
from pyutils.dict_utils import merge_dicts, get_nested, flatten_dict

__all__ = [
    "slugify",
    "truncate",
    "camel_to_snake",
    "chunk_list",
    "flatten_list",
    "remove_duplicates",
    "merge_dicts",
    "get_nested",
    "flatten_dict",
]
