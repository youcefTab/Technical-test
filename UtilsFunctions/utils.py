from collections import Counter
from typing import List, Tuple


def get_sorted_first_n_words(sentence: str, n: int) -> List[Tuple[str, int]]:
    """Get the first n words sorted by frequency and alphabetically."""

    # check the length of params
    if len(sentence) == 0 or n <= 0:
        print("Invalid input")
        return []

    # make it non case senstive (optional - depends on useCase)
    sentence_lowercase = sentence.lower()

    # Get the words of the sentence with the occurence by using Counter from python collections.
    words_list = sentence_lowercase.split()
    word_occurence_count = Counter(words_list)

    # Sort by frequency by descending order and alphabetically by asending order
    sorted_word_counts: List[Tuple[str, int]] = sorted(word_occurence_count.items(), key=lambda x: (-x[1], x[0]))  # type: ignore

    print("Sorted words completed", sorted_word_counts[:n])

    return sorted_word_counts[:n]
