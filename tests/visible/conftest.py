"""
Pytest configuration for Lab 3 visible tests.
Loads variant configuration if available.
"""

import json
import pytest
from pathlib import Path


@pytest.fixture(scope="session")
def variant_config():
    """Load student's variant configuration."""
    config_path = Path(__file__).parent.parent.parent / ".variant_config.json"
    if config_path.exists():
        with open(config_path) as f:
            return json.load(f)
    # Default values for testing without variant config
    return {
        "parameters": {
            "sample_count": 10,
            "rock_types": ["Granite", "Basalt", "Sandstone", "Schist"],
            "grade_range": {"min": 0.5, "max": 4.5}
        }
    }


@pytest.fixture
def expected_sample_count(variant_config):
    """Return expected sample count."""
    return variant_config["parameters"]["sample_count"]


@pytest.fixture
def expected_rock_types(variant_config):
    """Return expected rock types list."""
    return variant_config["parameters"]["rock_types"]


@pytest.fixture
def expected_grade_range(variant_config):
    """Return expected grade range."""
    return variant_config["parameters"]["grade_range"]


@pytest.fixture
def sample_data():
    """Provide sample test data for various tests."""
    return [
        {'sample_id': 'GEO-001', 'rock_type': 'Granite', 'grade': 2.45, 'depth': 150},
        {'sample_id': 'GEO-002', 'rock_type': 'Basalt', 'grade': 1.80, 'depth': 280},
        {'sample_id': 'GEO-003', 'rock_type': 'Granite', 'grade': 3.20, 'depth': 175},
        {'sample_id': 'GEO-004', 'rock_type': 'Sandstone', 'grade': 0.95, 'depth': 320},
        {'sample_id': 'GEO-005', 'rock_type': 'Basalt', 'grade': 2.10, 'depth': 410},
    ]


@pytest.fixture
def empty_sample_list():
    """Provide an empty sample list for edge case testing."""
    return []


@pytest.fixture
def single_sample():
    """Provide a single sample for edge case testing."""
    return [{'sample_id': 'GEO-001', 'rock_type': 'Granite', 'grade': 2.5, 'depth': 200}]
