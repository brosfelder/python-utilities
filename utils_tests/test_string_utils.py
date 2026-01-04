"""Tests for string_utils module."""

import pytest
from pyutils.string_utils import slugify, truncate, camel_to_snake


class TestSlugify:
    """Test cases for slugify function."""
    
    def test_basic_slugify(self):
        """Test basic string to slug conversion."""
        assert slugify("Hello World") == "hello-world"
    
    def test_slugify_with_special_chars(self):
        """Test slugify removes special characters."""
        assert slugify("Hello, World!") == "hello-world"
        assert slugify("Testing @#$ Special %^& Chars") == "testing-special-chars"
    
    def test_slugify_with_numbers(self):
        """Test slugify preserves numbers."""
        assert slugify("Python 3.11") == "python-311"
    
    def test_slugify_custom_separator(self):
        """Test slugify with custom separator."""
        assert slugify("Hello World", separator="_") == "hello_world"
        assert slugify("Test Case", separator=".") == "test.case"
    
    def test_slugify_multiple_spaces(self):
        """Test slugify handles multiple spaces."""
        assert slugify("Multiple   Spaces   Here") == "multiple-spaces-here"
    
    def test_slugify_empty_string(self):
        """Test slugify with empty string."""
        assert slugify("") == ""
    
    def test_slugify_already_slug(self):
        """Test slugify with already slugified string."""
        assert slugify("already-a-slug") == "already-a-slug"


class TestTruncate:
    """Test cases for truncate function."""
    
    def test_basic_truncate(self):
        """Test basic string truncation."""
        result = truncate("This is a long text", 10)
        assert len(result) == 10
        assert result == "This is..."
    
    def test_truncate_shorter_than_max(self):
        """Test truncate with string shorter than max_length."""
        text = "Short"
        assert truncate(text, 10) == "Short"
    
    def test_truncate_exact_length(self):
        """Test truncate with string exactly at max_length."""
        text = "Exactly10!"
        assert truncate(text, 10) == "Exactly10!"
    
    def test_truncate_custom_suffix(self):
        """Test truncate with custom suffix."""
        result = truncate("Long text here", 10, suffix=">>")
        assert result.endswith(">>")
        assert len(result) == 10
    
    def test_truncate_empty_suffix(self):
        """Test truncate with empty suffix."""
        result = truncate("Some text", 5, suffix="")
        assert result == "Some "
        assert len(result) == 5
    
    def test_truncate_long_suffix(self):
        """Test truncate when suffix is long."""
        result = truncate("Text", 5, suffix="...")
        assert len(result) == 5
    
    def test_truncate_empty_string(self):
        """Test truncate with empty string."""
        assert truncate("", 10) == ""


class TestCamelToSnake:
    """Test cases for camel_to_snake function."""
    
    def test_basic_camel_to_snake(self):
        """Test basic camelCase to snake_case conversion."""
        assert camel_to_snake("myVariableName") == "my_variable_name"
    
    def test_single_word(self):
        """Test camel_to_snake with single word."""
        assert camel_to_snake("variable") == "variable"
    
    def test_pascal_case(self):
        """Test camel_to_snake with PascalCase."""
        assert camel_to_snake("MyClassName") == "my_class_name"
    
    def test_consecutive_capitals(self):
        """Test camel_to_snake with consecutive capitals."""
        assert camel_to_snake("HTTPResponse") == "http_response"
        assert camel_to_snake("XMLParser") == "xml_parser"
    
    def test_numbers_in_name(self):
        """Test camel_to_snake with numbers."""
        assert camel_to_snake("variable2Name") == "variable2_name"
        assert camel_to_snake("get2ndValue") == "get2nd_value"
    
    def test_empty_string(self):
        """Test camel_to_snake with empty string."""
        assert camel_to_snake("") == ""
    
    def test_already_snake_case(self):
        """Test camel_to_snake with already snake_case."""
        assert camel_to_snake("already_snake_case") == "already_snake_case"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
