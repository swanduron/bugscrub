from source import information
from config import *

class DocToolkit(object):

    def __init__(self, informations):

        self.ori_info = informations
        self.ori_info = [i.lower().replace('[', ' ').replace(']', ' ') for i in self.ori_info]
        assert isinstance(self.ori_info, list)

    def get_word_freq(self):

        freq_dict = {}
        return_dict = {}
        self.total_info = ' '.join(self.ori_info)
        self.total_words = self.total_info.split()
        for word in self.total_words:
            word = self.remove_comma(word)
            if not word:
                continue
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1

        for word, freq in freq_dict.items():
            if freq > REPEAT_THRESHOLD:
                return_dict[word] = freq

        return return_dict

    def get_similarity(self, freq_dict):

        return_dict = {}
        for index in range(len(self.ori_info)):
            return_dict[index] = {}
            counter = 0
            for word in self.ori_info[index].split():
                word = self.remove_comma(word)
                if word in freq_dict:
                    counter += 1
            return_dict[index] = {'text': self.ori_info[index], 'level':counter}

        return return_dict

    def remove_comma(self, word):

        if word[-1] in IGNORE_CHAR and len(word) > 1 and word[:-1] not in IGNORE_WORDS:
            word = word[:-1]
        elif word[-1] in IGNORE_CHAR and len(word) == 1:
            word = ''
        elif word in IGNORE_WORDS:
            word = ''
        elif word[:-1] in IGNORE_WORDS:
            word = ''

        return word

if __name__ == '__main__':
    toolkit = DocToolkit(information)
    freq_dict = toolkit.get_word_freq()
    for index, content in toolkit.get_similarity(freq_dict).items():
        print(index, content['level'])