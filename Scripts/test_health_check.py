
from health_check import get_health_status


def test_low_usage_is_healthy():
    assert get_health_status(20, 40, 50) == "HEALTHY"


def test_high_cpu_is_warning():
    assert get_health_status(95, 40, 50) == "WARNING"


def test_high_memory_is_warning():
    assert get_health_status(20, 95, 50) == "WARNING"


def test_high_disk_is_warning():
    assert get_health_status(20, 40, 95) == "WARNING"


def test_threshold_is_warning():
    assert get_health_status(90, 20, 20) == "WARNING"
