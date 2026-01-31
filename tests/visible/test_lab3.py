"""
Lab 3 Visible Tests - Data Structures: Lists & Dictionaries
These tests verify basic functionality of list and dictionary operations.
"""

import sys
from pathlib import Path

# Add src directory to path
SRC_DIR = Path(__file__).parent.parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))


class TestTask1Lists:
    """Tests for Task 1: List Operations (lab3_lists.py)"""

    def test_lists_file_exists(self):
        """lab3_lists.py file should exist"""
        assert (SRC_DIR / "lab3_lists.py").exists(), "lab3_lists.py not found in src/"

    def test_create_depth_list_function_exists(self):
        """create_depth_list function should be defined"""
        from lab3_lists import create_depth_list
        assert callable(create_depth_list), "create_depth_list should be a function"

    def test_create_depth_list_returns_list(self):
        """create_depth_list should return a list"""
        from lab3_lists import create_depth_list
        result = create_depth_list(5)
        assert result is not None, "Function should not return None"
        assert isinstance(result, list), "Should return a list"

    def test_create_depth_list_correct_count(self):
        """create_depth_list should return correct number of items"""
        from lab3_lists import create_depth_list
        result = create_depth_list(8)
        if result is not None:
            assert len(result) == 8, f"Should return 8 items, got {len(result)}"

    def test_create_rock_type_list_function_exists(self):
        """create_rock_type_list function should be defined"""
        from lab3_lists import create_rock_type_list
        assert callable(create_rock_type_list), "create_rock_type_list should be a function"

    def test_create_rock_type_list_returns_list(self):
        """create_rock_type_list should return a list"""
        from lab3_lists import create_rock_type_list
        result = create_rock_type_list()
        assert result is not None, "Function should not return None"
        assert isinstance(result, list), "Should return a list"

    def test_demonstrate_indexing_function_exists(self):
        """demonstrate_indexing function should be defined"""
        from lab3_lists import demonstrate_indexing
        assert callable(demonstrate_indexing), "demonstrate_indexing should be a function"

    def test_demonstrate_indexing_returns_dict(self):
        """demonstrate_indexing should return a dictionary"""
        from lab3_lists import demonstrate_indexing
        test_list = [100, 200, 300, 400, 500]
        result = demonstrate_indexing(test_list)
        assert result is not None, "Function should not return None"
        assert isinstance(result, dict), "Should return a dictionary"

    def test_demonstrate_indexing_has_required_keys(self):
        """demonstrate_indexing should have required keys"""
        from lab3_lists import demonstrate_indexing
        test_list = [100, 200, 300, 400, 500]
        result = demonstrate_indexing(test_list)
        if result:
            required_keys = ['first', 'last', 'second', 'second_to_last']
            for key in required_keys:
                assert key in result, f"Result should have '{key}' key"

    def test_demonstrate_indexing_first_element(self):
        """demonstrate_indexing should correctly get first element"""
        from lab3_lists import demonstrate_indexing
        test_list = [100, 200, 300, 400, 500]
        result = demonstrate_indexing(test_list)
        if result:
            assert result.get('first') == 100, "First element should be 100"

    def test_demonstrate_indexing_last_element(self):
        """demonstrate_indexing should correctly get last element"""
        from lab3_lists import demonstrate_indexing
        test_list = [100, 200, 300, 400, 500]
        result = demonstrate_indexing(test_list)
        if result:
            assert result.get('last') == 500, "Last element should be 500"

    def test_demonstrate_slicing_function_exists(self):
        """demonstrate_slicing function should be defined"""
        from lab3_lists import demonstrate_slicing
        assert callable(demonstrate_slicing), "demonstrate_slicing should be a function"

    def test_demonstrate_slicing_returns_dict(self):
        """demonstrate_slicing should return a dictionary"""
        from lab3_lists import demonstrate_slicing
        test_list = [100, 200, 300, 400, 500, 600]
        result = demonstrate_slicing(test_list)
        assert result is not None, "Function should not return None"
        assert isinstance(result, dict), "Should return a dictionary"

    def test_calculate_depth_statistics_function_exists(self):
        """calculate_depth_statistics function should be defined"""
        from lab3_lists import calculate_depth_statistics
        assert callable(calculate_depth_statistics)

    def test_calculate_depth_statistics_returns_dict(self):
        """calculate_depth_statistics should return a dictionary"""
        from lab3_lists import calculate_depth_statistics
        test_list = [100, 200, 300, 400, 500]
        result = calculate_depth_statistics(test_list)
        assert result is not None, "Function should not return None"
        assert isinstance(result, dict), "Should return a dictionary"


class TestTask2Dictionaries:
    """Tests for Task 2: Dictionary Operations (lab3_dictionaries.py)"""

    def test_dictionaries_file_exists(self):
        """lab3_dictionaries.py file should exist"""
        assert (SRC_DIR / "lab3_dictionaries.py").exists(), "lab3_dictionaries.py not found"

    def test_create_sample_record_function_exists(self):
        """create_sample_record function should be defined"""
        from lab3_dictionaries import create_sample_record
        assert callable(create_sample_record)

    def test_create_sample_record_returns_dict(self):
        """create_sample_record should return a dictionary"""
        from lab3_dictionaries import create_sample_record
        result = create_sample_record('GEO-001', 'Granite', 2.5, 150)
        assert result is not None, "Function should not return None"
        assert isinstance(result, dict), "Should return a dictionary"

    def test_create_sample_record_has_required_keys(self):
        """create_sample_record should have required keys"""
        from lab3_dictionaries import create_sample_record
        result = create_sample_record('GEO-001', 'Granite', 2.5, 150)
        if result:
            for key in ['sample_id', 'rock_type', 'grade', 'depth']:
                assert key in result, f"Missing key: {key}"

    def test_create_sample_record_correct_values(self):
        """create_sample_record should store correct values"""
        from lab3_dictionaries import create_sample_record
        result = create_sample_record('GEO-001', 'Granite', 2.5, 150)
        if result:
            assert result['sample_id'] == 'GEO-001'
            assert result['rock_type'] == 'Granite'
            assert result['grade'] == 2.5
            assert result['depth'] == 150

    def test_access_sample_values_function_exists(self):
        """access_sample_values function should be defined"""
        from lab3_dictionaries import access_sample_values
        assert callable(access_sample_values)

    def test_demonstrate_dictionary_methods_function_exists(self):
        """demonstrate_dictionary_methods function should be defined"""
        from lab3_dictionaries import demonstrate_dictionary_methods
        assert callable(demonstrate_dictionary_methods)

    def test_update_sample_function_exists(self):
        """update_sample function should be defined"""
        from lab3_dictionaries import update_sample
        assert callable(update_sample)

    def test_update_sample_creates_copy(self):
        """update_sample should not modify original"""
        from lab3_dictionaries import update_sample
        original = {'sample_id': 'GEO-001', 'grade': 2.0}
        result = update_sample(original, {'grade': 3.0})
        if result:
            assert original['grade'] == 2.0, "Original should not be modified"

    def test_create_nested_sample_database_function_exists(self):
        """create_nested_sample_database function should be defined"""
        from lab3_dictionaries import create_nested_sample_database
        assert callable(create_nested_sample_database)

    def test_create_nested_sample_database_returns_dict(self):
        """create_nested_sample_database should return a dictionary"""
        from lab3_dictionaries import create_nested_sample_database
        result = create_nested_sample_database()
        assert result is not None, "Function should not return None"
        assert isinstance(result, dict), "Should return a dictionary"

    def test_filter_by_minimum_grade_function_exists(self):
        """filter_by_minimum_grade function should be defined"""
        from lab3_dictionaries import filter_by_minimum_grade
        assert callable(filter_by_minimum_grade)


class TestTask3SampleManager:
    """Tests for Task 3: Sample Collection Manager (lab3_sample_manager.py)"""

    def test_sample_manager_file_exists(self):
        """lab3_sample_manager.py file should exist"""
        assert (SRC_DIR / "lab3_sample_manager.py").exists()

    def test_create_sample_collection_function_exists(self):
        """create_sample_collection function should be defined"""
        from lab3_sample_manager import create_sample_collection
        assert callable(create_sample_collection)

    def test_create_sample_collection_returns_list(self):
        """create_sample_collection should return an empty list"""
        from lab3_sample_manager import create_sample_collection
        result = create_sample_collection()
        assert result is not None, "Function should not return None"
        assert isinstance(result, list), "Should return a list"
        assert len(result) == 0, "Should return empty list"

    def test_add_sample_function_exists(self):
        """add_sample function should be defined"""
        from lab3_sample_manager import add_sample
        assert callable(add_sample)

    def test_add_sample_adds_to_collection(self):
        """add_sample should add a sample to the collection"""
        from lab3_sample_manager import create_sample_collection, add_sample
        collection = create_sample_collection()
        if collection is not None:
            result = add_sample(collection, 'GEO-001', 'Granite', 2.5, 150)
            if result is not None:
                assert len(result) == 1, "Collection should have 1 sample"

    def test_find_sample_by_id_function_exists(self):
        """find_sample_by_id function should be defined"""
        from lab3_sample_manager import find_sample_by_id
        assert callable(find_sample_by_id)

    def test_find_sample_by_id_returns_correct_sample(self):
        """find_sample_by_id should return the correct sample"""
        from lab3_sample_manager import create_sample_collection, add_sample, find_sample_by_id
        collection = create_sample_collection()
        if collection is not None:
            add_sample(collection, 'GEO-001', 'Granite', 2.5, 150)
            result = find_sample_by_id(collection, 'GEO-001')
            if result is not None:
                assert result['sample_id'] == 'GEO-001'

    def test_find_sample_by_id_returns_none_when_not_found(self):
        """find_sample_by_id should return None for non-existent ID"""
        from lab3_sample_manager import create_sample_collection, find_sample_by_id
        collection = create_sample_collection()
        if collection is not None:
            result = find_sample_by_id(collection, 'NON-EXISTENT')
            assert result is None, "Should return None for non-existent ID"

    def test_find_by_rock_type_function_exists(self):
        """find_by_rock_type function should be defined"""
        from lab3_sample_manager import find_by_rock_type
        assert callable(find_by_rock_type)

    def test_update_grade_function_exists(self):
        """update_grade function should be defined"""
        from lab3_sample_manager import update_grade
        assert callable(update_grade)

    def test_remove_sample_function_exists(self):
        """remove_sample function should be defined"""
        from lab3_sample_manager import remove_sample
        assert callable(remove_sample)

    def test_get_unique_rock_types_function_exists(self):
        """get_unique_rock_types function should be defined"""
        from lab3_sample_manager import get_unique_rock_types
        assert callable(get_unique_rock_types)


class TestTask4Statistics:
    """Tests for Task 4: Computing Statistics (lab3_statistics.py)"""

    def test_statistics_file_exists(self):
        """lab3_statistics.py file should exist"""
        assert (SRC_DIR / "lab3_statistics.py").exists()

    def test_calculate_average_grade_function_exists(self):
        """calculate_average_grade function should be defined"""
        from lab3_statistics import calculate_average_grade
        assert callable(calculate_average_grade)

    def test_calculate_average_grade_correct_result(self, sample_data):
        """calculate_average_grade should return correct average"""
        from lab3_statistics import calculate_average_grade
        result = calculate_average_grade(sample_data)
        if result is not None:
            expected = (2.45 + 1.80 + 3.20 + 0.95 + 2.10) / 5
            assert abs(result - expected) < 0.01, f"Expected {expected}, got {result}"

    def test_calculate_average_grade_empty_list(self, empty_sample_list):
        """calculate_average_grade should handle empty list"""
        from lab3_statistics import calculate_average_grade
        result = calculate_average_grade(empty_sample_list)
        assert result is None, "Should return None for empty list"

    def test_find_depth_range_function_exists(self):
        """find_depth_range function should be defined"""
        from lab3_statistics import find_depth_range
        assert callable(find_depth_range)

    def test_find_depth_range_correct_result(self, sample_data):
        """find_depth_range should return correct min and max"""
        from lab3_statistics import find_depth_range
        result = find_depth_range(sample_data)
        if result is not None:
            assert result[0] == 150, f"Min depth should be 150, got {result[0]}"
            assert result[1] == 410, f"Max depth should be 410, got {result[1]}"

    def test_count_by_rock_type_function_exists(self):
        """count_by_rock_type function should be defined"""
        from lab3_statistics import count_by_rock_type
        assert callable(count_by_rock_type)

    def test_count_by_rock_type_correct_counts(self, sample_data):
        """count_by_rock_type should return correct counts"""
        from lab3_statistics import count_by_rock_type
        result = count_by_rock_type(sample_data)
        if result is not None:
            assert result.get('Granite') == 2, "Should have 2 Granite samples"
            assert result.get('Basalt') == 2, "Should have 2 Basalt samples"
            assert result.get('Sandstone') == 1, "Should have 1 Sandstone sample"

    def test_get_high_grade_samples_function_exists(self):
        """get_high_grade_samples function should be defined"""
        from lab3_statistics import get_high_grade_samples
        assert callable(get_high_grade_samples)

    def test_get_high_grade_samples_correct_filtering(self, sample_data):
        """get_high_grade_samples should filter correctly"""
        from lab3_statistics import get_high_grade_samples
        result = get_high_grade_samples(sample_data, 2.0)
        if result is not None:
            # Grades above 2.0: 2.45, 3.20, 2.10
            assert len(result) == 3, f"Should have 3 samples above 2.0, got {len(result)}"

    def test_calculate_average_by_rock_type_function_exists(self):
        """calculate_average_by_rock_type function should be defined"""
        from lab3_statistics import calculate_average_by_rock_type
        assert callable(calculate_average_by_rock_type)


class TestTask5Filters:
    """Tests for Task 5: Filtering and Sorting (lab3_filters.py)"""

    def test_filters_file_exists(self):
        """lab3_filters.py file should exist"""
        assert (SRC_DIR / "lab3_filters.py").exists()

    def test_filter_by_depth_range_function_exists(self):
        """filter_by_depth_range function should be defined"""
        from lab3_filters import filter_by_depth_range
        assert callable(filter_by_depth_range)

    def test_filter_by_depth_range_correct_filtering(self, sample_data):
        """filter_by_depth_range should filter correctly"""
        from lab3_filters import filter_by_depth_range
        result = filter_by_depth_range(sample_data, 200, 350)
        if result is not None:
            # Depths in range [200, 350]: 280, 320
            assert len(result) == 2, f"Should have 2 samples, got {len(result)}"

    def test_filter_by_rock_types_function_exists(self):
        """filter_by_rock_types function should be defined"""
        from lab3_filters import filter_by_rock_types
        assert callable(filter_by_rock_types)

    def test_filter_by_rock_types_correct_filtering(self, sample_data):
        """filter_by_rock_types should filter correctly"""
        from lab3_filters import filter_by_rock_types
        result = filter_by_rock_types(sample_data, ['Granite', 'Basalt'])
        if result is not None:
            assert len(result) == 4, f"Should have 4 samples, got {len(result)}"

    def test_sort_by_grade_function_exists(self):
        """sort_by_grade function should be defined"""
        from lab3_filters import sort_by_grade
        assert callable(sort_by_grade)

    def test_sort_by_grade_ascending(self, sample_data):
        """sort_by_grade should sort ascending correctly"""
        from lab3_filters import sort_by_grade
        result = sort_by_grade(sample_data, descending=False)
        if result is not None:
            grades = [s['grade'] for s in result]
            assert grades == sorted(grades), "Should be sorted ascending"

    def test_sort_by_grade_descending(self, sample_data):
        """sort_by_grade should sort descending correctly"""
        from lab3_filters import sort_by_grade
        result = sort_by_grade(sample_data, descending=True)
        if result is not None:
            grades = [s['grade'] for s in result]
            assert grades == sorted(grades, reverse=True), "Should be sorted descending"

    def test_sort_by_grade_does_not_modify_original(self, sample_data):
        """sort_by_grade should not modify original list"""
        from lab3_filters import sort_by_grade
        original_first = sample_data[0]['grade']
        sort_by_grade(sample_data, descending=True)
        assert sample_data[0]['grade'] == original_first, "Should not modify original"

    def test_get_top_n_by_grade_function_exists(self):
        """get_top_n_by_grade function should be defined"""
        from lab3_filters import get_top_n_by_grade
        assert callable(get_top_n_by_grade)

    def test_get_top_n_by_grade_correct_result(self, sample_data):
        """get_top_n_by_grade should return top N samples"""
        from lab3_filters import get_top_n_by_grade
        result = get_top_n_by_grade(sample_data, 2)
        if result is not None:
            assert len(result) == 2, "Should return 2 samples"
            # Top 2 grades should be 3.20 and 2.45
            grades = [s['grade'] for s in result]
            assert 3.20 in grades, "Should include highest grade (3.20)"
            assert 2.45 in grades, "Should include second highest grade (2.45)"

    def test_group_by_rock_type_function_exists(self):
        """group_by_rock_type function should be defined"""
        from lab3_filters import group_by_rock_type
        assert callable(group_by_rock_type)

    def test_group_by_rock_type_correct_grouping(self, sample_data):
        """group_by_rock_type should group samples correctly"""
        from lab3_filters import group_by_rock_type
        result = group_by_rock_type(sample_data)
        if result is not None:
            assert 'Granite' in result, "Should have Granite group"
            assert len(result['Granite']) == 2, "Should have 2 Granite samples"

    def test_extract_field_function_exists(self):
        """extract_field function should be defined"""
        from lab3_filters import extract_field
        assert callable(extract_field)

    def test_extract_field_correct_values(self, sample_data):
        """extract_field should extract correct values"""
        from lab3_filters import extract_field
        result = extract_field(sample_data, 'grade')
        if result is not None:
            expected = [2.45, 1.80, 3.20, 0.95, 2.10]
            assert result == expected, f"Expected {expected}, got {result}"
