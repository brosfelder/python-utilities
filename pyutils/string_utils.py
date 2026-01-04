"""String manipulation utilities."""


def slugify(text: str, separator: str = "-") -> str:
    """
    Convert a string to a URL-friendly slug.
    
    Args:
        text: Input text to slugify
        separator: Character to use as separator (default: "-")
        
    Returns:
        Slugified string (lowercase, alphanumeric, with separators)
        
    Example:
        >>> slugify("Hello World!")
        'hello-world'
    """
    # TODO: Implement slugify logic
    # raise NotImplementedError("slugify not yet implemented")
    return text.lower().strip().replace('!','').replace('?','').replace('.','').replace(' ', '-')


def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate a string to a maximum length.
    
    Args:
        text: Input text to truncate
        max_length: Maximum length of the output string
        suffix: String to append if truncated (default: "...")
        
    Returns:
        Truncated string with suffix if needed
        
    Example:
        >>> truncate("This is a long text", 10)
        'This is...'
    """
    if(len(text) <= max_length):
        return text
    else:
        return text[:max_length - len(suffix)] + suffix

def camel_to_snake(text: str) -> str:
    """
    Convert camelCase to snake_case.
    
    Args:
        text: Input text in camelCase
        
    Returns:
        String in snake_case format
        
    Example:
        >>> camel_to_snake("myVariableName")
        'my_variable_name'
    """
    # TODO: Implement camel_to_snake logic
    raise NotImplementedError("camel_to_snake not yet implemented")
