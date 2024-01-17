import Halari_Shanpru as name_point

def test_length_greater_than_one():
    assert len(name_point.hi_my_name_is()) > 1

def test_output_is_alphabetic():
    assert name_point.hi_my_name_is().isalpha()

def test_output_is_equal_to_name():
    assert name_point.hi_my_name_is() == "HALARI"

def test_output_is_in_uppercase():
    assert name_point.hi_my_name_is().isupper()


def test_output_has_correct_length():
    assert len(name_point.hi_my_name_is()) == 6

def test_output_starts_with_specific_letter():
    assert name_point.hi_my_name_is().startswith("H")

def test_output_ends_with_specific_letter():
    assert name_point.hi_my_name_is().endswith("I")

def test_output_is_not_empty():
    assert name_point.hi_my_name_is() != ""