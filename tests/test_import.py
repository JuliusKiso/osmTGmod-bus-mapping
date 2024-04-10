"""Test osmTGmod Bus Mapping."""

import osmtgmod_bus_mapping


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(osmtgmod_bus_mapping.__name__, str)
