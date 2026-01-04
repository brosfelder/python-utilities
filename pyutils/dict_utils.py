"""Dictionary manipulation utilities."""

from typing import Dict, Any, Optional


def merge_dicts(*dicts: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge multiple dictionaries into one.
    
    Args:
        *dicts: Variable number of dictionaries to merge
        
    Returns:
        Merged dictionary (later dicts override earlier ones)
        
    Example:
        >>> merge_dicts({'a': 1}, {'b': 2}, {'a': 3})
        {'a': 3, 'b': 2}
    """
    # TODO: Implement merge_dicts logic
    raise NotImplementedError("merge_dicts not yet implemented")


def get_nested(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    """
    Get a value from a nested dictionary using dot notation.
    
    Args:
        data: Dictionary to search
        path: Dot-separated path (e.g., "user.address.city")
        default: Default value if path not found
        
    Returns:
        Value at the specified path or default
        
    Example:
        >>> get_nested({'user': {'name': 'John'}}, 'user.name')
        'John'
    """
    # TODO: Implement get_nested logic
    raise NotImplementedError("get_nested not yet implemented")


def flatten_dict(data: Dict[str, Any], separator: str = ".") -> Dict[str, Any]:
    """
    Flatten a nested dictionary using dot notation for keys.
    
    Args:
        data: Nested dictionary to flatten
        separator: Separator for nested keys (default: ".")
        
    Returns:
        Flattened dictionary
        
    Example:
        >>> flatten_dict({'a': {'b': {'c': 1}}})
        {'a.b.c': 1}
    """
    # TODO: Implement flatten_dict logic
    raise NotImplementedError("flatten_dict not yet implemented")
