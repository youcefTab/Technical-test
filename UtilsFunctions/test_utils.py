from UtilsFunctions.utils import get_sorted_first_n_words


def test_get_sorted_first_n_words_no_sentence_provided():
    assert get_sorted_first_n_words("", 5) == []


def test_get_sorted_first_n_words_no_words_provided():
    assert get_sorted_first_n_words(" ", 5) == []


def test_get_sorted_first_n_words_no_number_provided():
    assert get_sorted_first_n_words("This This is a a test test", 0) == []


def test_get_sorted_first_n_lowercase_respected():
    expected_output = [("zblah", 3), ("bar", 2), ("baz", 2)]
    assert get_sorted_first_n_words("bar baz foo foo ZBLAH ZBLAH zblah baz toto bar", 3) == expected_output


def test_get_sorted_first_n_normal_case_usage():
    expected_output = [("zblah", 3), ("bar", 2), ("baz", 2)]
    assert get_sorted_first_n_words("bar baz foo foo zblah zblah zblah baz toto bar", 3) == expected_output


def test_get_sorted_first_n_words_alphabetic_order_respected():
    expected_output = [("foo", 2), ("aaa", 1), ("bar", 1)]
    assert get_sorted_first_n_words("foo aaa bar baz foo tro", 3) == expected_output


def test_get_sorted_first_n_words_case_insensitive_lowercase__alphabetic_order_respected():
    expected_output = [("foo", 2), ("aaa", 1), ("bar", 1)]
    assert get_sorted_first_n_words("foo AAA bar baz foo tro", 3) == expected_output


def test_get_sorted_first_n_words_one_word_string():
    expected_output = [("fooAAAbarbazfootro", 1)]
    assert get_sorted_first_n_words("fooAAAbarbazfootro", 3) == expected_output
