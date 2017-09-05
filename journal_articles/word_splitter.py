import enchant

"""
This is a method for finding the best possible splits for a string that is missing spaces.

Parameters:
-----------
standard_dict : directory, Whether or not you want to use a standard pyenchant dictionary.
incl_list : list, A list of words you want to include as possible solutions to splits (eg. proper nouns)

num_of_words : int, Number of word splits you want to check up to.


"""

class WordSplitter(object):
    def __init__(self, standard_dict = None, incl_list = None, num_of_words = 3):
        self.incl_list = incl_list
        if not standard_dict:
            self.pwl = enchant.request_pwl_dict(standard_dict)
        else:
            self.pwl = enchant.Dict("en_US")
        self.num_of_words = num_of_words

    def _partitions(self, s, k):
        """
        Gets all partitions of string.

        Parameters:
        -----------
        s : string, The string to be partitioned.
        k: Number of partitions to return.
        """
        if not k:
            yield [s]
            return
        for i in range(len(s) + 1):
            for tail in self._partitions(s[i:], k - 1):
                yield [s[:i]] + tail

    def _get_best_score(self, p):
        """
        Get the best scoring partition for the current number of partions.

        Parameters:
        -----------
        p : list, The list of partitions of the string.

        """
        scores = []
        for group in p:
            right = 0
            for part in group:
                if part:
                    chk = self.pwl.check(part)
                    if not chk and self.incl_list:
                        if self.incl_list.count(part) > 1:
                            chk = True
                    if chk:
                        right += 1
            scores.append((group, right))
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[0]

    def get_word_splits(self, word):
        """
        Get the most likely correct list of words for the input string.

        Parameters:
        -----------
        word : string, Misspelled word to be checked for correct sub-strings.
        """
        best = []
        for group_len in range(self.num_of_words):
            p = list(self._partitions(word, group_len))
            top = self._get_best_score(p)
            if len(top[0]) == top[1]:
                return top[0]
            best.append(top)
        best.sort(key=lambda x: x[1], reverse=True)
        return best[0][0]
