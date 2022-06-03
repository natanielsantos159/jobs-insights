from src.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("src/jobs.csv", "javascript") == 122
    assert count_ocurrences("src/jobs.csv", "python") == 1639
    assert count_ocurrences("src/jobs.csv", "gap") == 175
    assert count_ocurrences("src/jobs.csv", "bridge") == 73
