import unittest
import homeworks


class TestsForFunctions(unittest.TestCase):
    def test_sum_of_integers_in_strings_positive(self):
        result: list = homeworks.sum_of_integers_in_strings(['1,2,3,4', '1,2,3,4,50', '4,5,76,2'])
        self.assertEqual(result, [10, 60, 87])

    def test_sum_of_integers_in_strings_negative(self):
        result: list = homeworks.sum_of_integers_in_strings(['1,2,3,4', '1,2,3,4,50', 'string,5,76,2'])
        self.assertEqual(result, [10, 60, "Can't do this"])

    def test_even_digits_sum_positive(self):
        result: int = homeworks.even_digits_sum([1, 2, 3, 4, 5, 6])
        self.assertEqual(result, 12)

    def test_even_digits_sum_negative(self):
        result: int = homeworks.even_digits_sum([1, 3, 5, 7])
        self.assertEqual(result, 0)

    def test_separate_sentences_in_text_positive(self):
        result: list = homeworks.separate_sentences_in_text(
            "The sun set behind the mountains, casting a warm orange glow over the valley. Birds chirped softly as "
            "they settled into the trees for the night. In the distance, the sound of a river could be heard, "
            "its gentle flow bringing a sense of peace to the quiet evening.")
        self.assertEqual(result, ['The sun set behind the mountains, casting a warm orange glow over the valley.',
                                  'Birds chirped softly as they settled into the trees for the night.',
                                  'In the distance, the sound of a river could be heard, its gentle flow bringing a '
                                  'sense of peace to the quiet evening.'])

    def test_separate_sentences_in_text_negative(self):
        result: list = homeworks.separate_sentences_in_text("")
        self.assertEqual(result, [""])

    def test_count_uppercase_positive(self):
        result: int = homeworks.count_uppercase("The Sky turned pink as the Sun dipped below the Horizon.")
        self.assertEqual(result, 4)

    def test_count_uppercase_negative(self):
        result: int = homeworks.count_uppercase("the sky turned pink as the sun dipped below the horizon.")
        self.assertEqual(result, 0)

    def test_remove_extra_spaces_positive(self):
        result: str = homeworks.remove_extra_spaces("The  moonlight   softly illuminated  the quiet forest    path.")
        self.assertEqual(result, "The moonlight softly illuminated the quiet forest path.")

    def test_remove_extra_spaces_negative(self):
        with self.assertRaises(AttributeError):
            homeworks.remove_extra_spaces(12345)


if __name__ == '__main__':
    unittest.main()
