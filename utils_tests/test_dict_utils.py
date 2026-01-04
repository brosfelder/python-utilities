"""Tests for dict_utils module."""

import pytest
from pyutils.dict_utils import merge_dicts, get_nested, flatten_dict


class TestMergeDicts:
    """Test cases for merge_dicts function."""
    
    def test_basic_merge(self):
        """Test basic dictionary merging."""
        result = merge_dicts({'a': 1}, {'b': 2})
        assert result == {'a': 1, 'b': 2}
    
    def test_merge_with_override(self):
        """Test merge with overlapping keys."""
        result = merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
        assert result == {'a': 1, 'b': 3, 'c': 4}
    
    def test_merge_multiple_dicts(self):
        """Test merging more than two dicts."""
        result = merge_dicts({'a': 1}, {'b': 2}, {'c': 3})
        assert result == {'a': 1, 'b': 2, 'c': 3}
    
    def test_merge_empty_dicts(self):
        """Test merging empty dictionaries."""
        result = merge_dicts({}, {})
        assert result == {}
    
    def test_merge_with_empty(self):
        """Test merge with one empty dict."""
        result = merge_dicts({'a': 1}, {})
        assert result == {'a': 1}
    
    def test_merge_priority(self):
        """Test that later dicts override earlier ones."""
        result = merge_dicts({'a': 1}, {'a': 2}, {'a': 3})
        assert result['a'] == 3
    
    def test_merge_complex_values(self):
        """Test merge with complex value types."""
        result = merge_dicts(
            {'a': [1, 2], 'b': {'x': 1}},
            {'c': 'test'}
        )
        assert result == {'a': [1, 2], 'b': {'x': 1}, 'c': 'test'}


class TestGetNested:
    """Test cases for get_nested function."""
    
    def test_basic_nested_get(self):
        """Test basic nested value retrieval."""
        data = {'user': {'name': 'John', 'age': 30}}
        assert get_nested(data, 'user.name') == 'John'
    
    def test_deeply_nested_get(self):
        """Test deeply nested value retrieval."""
        data = {'a': {'b': {'c': {'d': 42}}}}
        assert get_nested(data, 'a.b.c.d') == 42
    
    def test_get_top_level(self):
        """Test getting top-level value."""
        data = {'name': 'Alice'}
        assert get_nested(data, 'name') == 'Alice'
    
    def test_get_nonexistent_with_default(self):
        """Test getting non-existent path with default."""
        data = {'a': 1}
        assert get_nested(data, 'b.c', default='not found') == 'not found'
    
    def test_get_nonexistent_without_default(self):
        """Test getting non-existent path without default."""
        data = {'a': 1}
        assert get_nested(data, 'b.c') is None
    
    def test_get_partial_path(self):
        """Test getting partial nested structure."""
        data = {'user': {'address': {'city': 'NYC', 'zip': '10001'}}}
        assert get_nested(data, 'user.address') == {'city': 'NYC', 'zip': '10001'}
    
    def test_get_with_list_values(self):
        """Test getting nested value with lists."""
        data = {'items': [1, 2, 3]}
        assert get_nested(data, 'items') == [1, 2, 3]
    
    def test_get_empty_path(self):
        """Test with empty path."""
        data = {'a': 1}
        assert get_nested(data, '') == data


class TestFlattenDict:
    """Test cases for flatten_dict function."""
    
    def test_basic_flatten(self):
        """Test basic dictionary flattening."""
        data = {'a': {'b': 1, 'c': 2}}
        result = flatten_dict(data)
        assert result == {'a.b': 1, 'a.c': 2}
    
    def test_deeply_nested_flatten(self):
        """Test deeply nested dictionary flattening."""
        data = {'a': {'b': {'c': {'d': 1}}}}
        result = flatten_dict(data)
        assert result == {'a.b.c.d': 1}
    
    def test_flatten_mixed_levels(self):
        """Test flatten with mixed nesting levels."""
        data = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
        result = flatten_dict(data)
        assert result == {'a': 1, 'b.c': 2, 'b.d.e': 3}
    
    def test_flatten_custom_separator(self):
        """Test flatten with custom separator."""
        data = {'a': {'b': 1}}
        result = flatten_dict(data, separator='_')
        assert result == {'a_b': 1}
    
    def test_flatten_empty_dict(self):
        """Test flatten with empty dictionary."""
        result = flatten_dict({})
        assert result == {}
    
    def test_flatten_no_nesting(self):
        """Test flatten with already flat dict."""
        data = {'a': 1, 'b': 2, 'c': 3}
        result = flatten_dict(data)
        assert result == {'a': 1, 'b': 2, 'c': 3}
    
    def test_flatten_complex_values(self):
        """Test flatten preserves non-dict values."""
        data = {
            'user': {
                'name': 'John',
                'hobbies': ['reading', 'coding'],
                'active': True
            }
        }
        result = flatten_dict(data)
        assert result == {
            'user.name': 'John',
            'user.hobbies': ['reading', 'coding'],
            'user.active': True
        }
    
    def test_flatten_multiple_branches(self):
        """Test flatten with multiple nested branches."""
        data = {
            'user': {'name': 'Alice', 'age': 25},
            'settings': {'theme': 'dark', 'notifications': True}
        }
        result = flatten_dict(data)
        assert result == {
            'user.name': 'Alice',
            'user.age': 25,
            'settings.theme': 'dark',
            'settings.notifications': True
        }


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
