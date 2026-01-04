"""Tests for list_utils module."""

import pytest
from pyutils.list_utils import chunk_list, flatten_list, remove_duplicates


class TestChunkList:
    """Test cases for chunk_list function."""
    
    def test_basic_chunking(self):
        """Test basic list chunking."""
        result = chunk_list([1, 2, 3, 4, 5, 6], 2)
        assert result == [[1, 2], [3, 4], [5, 6]]
    
    def test_chunk_with_remainder(self):
        """Test chunking when list doesn't divide evenly."""
        result = chunk_list([1, 2, 3, 4, 5], 2)
        assert result == [[1, 2], [3, 4], [5]]
    
    def test_chunk_size_larger_than_list(self):
        """Test chunking with chunk size larger than list."""
        result = chunk_list([1, 2, 3], 5)
        assert result == [[1, 2, 3]]
    
    def test_chunk_size_one(self):
        """Test chunking with size 1."""
        result = chunk_list([1, 2, 3], 1)
        assert result == [[1], [2], [3]]
    
    def test_empty_list(self):
        """Test chunking empty list."""
        result = chunk_list([], 2)
        assert result == []
    
    def test_chunk_with_strings(self):
        """Test chunking list of strings."""
        result = chunk_list(['a', 'b', 'c', 'd'], 2)
        assert result == [['a', 'b'], ['c', 'd']]
    
    def test_chunk_equal_to_list_size(self):
        """Test chunk size equal to list size."""
        result = chunk_list([1, 2, 3], 3)
        assert result == [[1, 2, 3]]
    
    def test_chunk_size_zero(self):
        """Test chunking with chunk size of zero."""
        with pytest.raises(ValueError):
            chunk_list([1, 2, 3], 0)
    
    def test_chunk_size_negative(self):
        """Test chunking with negative chunk size."""
        with pytest.raises(ValueError):
            chunk_list([1, 2, 3], -1)
    
    def test_chunk_size_float(self):
        """Test chunking with float chunk size."""
        with pytest.raises(TypeError):
            chunk_list([1, 2, 3], 2.5)


class TestFlattenList:
    """Test cases for flatten_list function."""
    
    def test_basic_flatten(self):
        """Test basic list flattening."""
        result = flatten_list([[1, 2], [3, 4], [5]])
        assert result == [1, 2, 3, 4, 5]
    
    def test_flatten_single_level(self):
        """Test flatten with already flat list."""
        result = flatten_list([1, 2, 3, 4])
        assert result == [1, 2, 3, 4]
    
    def test_flatten_empty_sublists(self):
        """Test flatten with empty sublists."""
        result = flatten_list([[1, 2], [], [3, 4], []])
        assert result == [1, 2, 3, 4]
    
    def test_flatten_nested_deeper(self):
        """Test flatten with deeply nested lists."""
        result = flatten_list([[1, [2, 3]], [4, [5, 6]]])
        assert result == [1, 2, 3, 4, 5, 6]
    
    def test_flatten_empty_list(self):
        """Test flatten with empty list."""
        result = flatten_list([])
        assert result == []
    
    def test_flatten_mixed_types(self):
        """Test flatten with mixed data types."""
        result = flatten_list([[1, 'a'], [2, 'b'], [3, 'c']])
        assert result == [1, 'a', 2, 'b', 3, 'c']
    
    def test_flatten_single_sublist(self):
        """Test flatten with single sublist."""
        result = flatten_list([[1, 2, 3]])
        assert result == [1, 2, 3]


class TestRemoveDuplicates:
    """Test cases for remove_duplicates function."""
    
    def test_basic_remove_duplicates(self):
        """Test basic duplicate removal."""
        result = remove_duplicates([1, 2, 2, 3, 1])
        assert result == [1, 2, 3]
    
    def test_preserve_order(self):
        """Test that order is preserved."""
        result = remove_duplicates([3, 1, 2, 1, 3, 2], preserve_order=True)
        assert result == [3, 1, 2]
    
    def test_no_duplicates(self):
        """Test list without duplicates."""
        result = remove_duplicates([1, 2, 3, 4])
        assert result == [1, 2, 3, 4]
    
    def test_all_duplicates(self):
        """Test list with all same elements."""
        result = remove_duplicates([5, 5, 5, 5])
        assert result == [5]
    
    def test_empty_list(self):
        """Test empty list."""
        result = remove_duplicates([])
        assert result == []
    
    def test_string_duplicates(self):
        """Test duplicate removal with strings."""
        result = remove_duplicates(['a', 'b', 'a', 'c', 'b'])
        assert result == ['a', 'b', 'c']
    
    def test_preserve_order_false(self):
        """Test without preserving order."""
        result = remove_duplicates([3, 1, 2, 1, 3], preserve_order=False)
        assert set(result) == {1, 2, 3}
        assert len(result) == 3
    
    def test_single_element(self):
        """Test list with single element."""
        result = remove_duplicates([1])
        assert result == [1]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
