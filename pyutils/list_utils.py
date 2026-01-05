"""List manipulation utilities."""

from typing import List, Any, TypeVar

T = TypeVar('T')


def chunk_list(data: List[T], chunk_size: int) -> List[List[T]]:
    """
    Split a list into chunks of specified size.
    
    Args:
        data: List to split into chunks
        chunk_size: Size of each chunk
        
    Returns:
        List of chunks (each chunk is a list)
        
    Example:
        >>> chunk_list([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size parameter must be positive")
    return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]


def flatten_list(nested_list: List[Any]) -> List[Any]:
    """
    Flatten a nested list into a single-level list.
    
    Args:
        nested_list: Nested list to flatten
        
    Returns:
        Flattened list
        
    Example:
        >>> flatten_list([[1, 2], [3, 4], [5]])
        [1, 2, 3, 4, 5]
    """
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

def remove_duplicates(data: List[T], preserve_order: bool = True) -> List[T]:
    """
    Remove duplicates from a list.
    
    Args:
        data: List with potential duplicates
        preserve_order: Whether to maintain original order (default: True)
        
    Returns:
        List without duplicates
        
    Example:
        >>> remove_duplicates([1, 2, 2, 3, 1])
        [1, 2, 3]
    """
    if preserve_order:
        return list(dict.fromkeys(data))
    else:
        return list(set(data))