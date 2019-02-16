from source import information
from config import *
import re

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
        elif word[:-1] in IGNORE_WORDS and len(word) <= 2:
            word = ''
        # elif re.findall('^\d+$', word):
        #     word = ''

        return word

if __name__ == '__main__':
    toolkit = DocToolkit(information)
    freq_dict = toolkit.get_word_freq()

    counter = 0
    level_list = []

    max = 0
    content = ''
    for index, content in toolkit.get_similarity(freq_dict).items():
        print(index, content['level'])
        counter += content['level']
        level_list.append(content['level'])
        if content['level'] > max:
            max = content['level']
            content = content['text']
    # print(max)
    # print(content)
    print('-'*50)
    print(counter)
    print(level_list)
    dif = 20/len(level_list)
    pingjun = counter/len(level_list)
    print(dif, pingjun)
    print('1 sigma:', pingjun-dif, pingjun+dif)
    print('2 sigma:', pingjun-2*dif, pingjun+2*dif)
    print('3 sigma:', pingjun - 3*dif, pingjun + 3*dif)
    print(list(filter(lambda i: i>pingjun-dif, level_list)))
    print(len(list(filter(lambda i: i>pingjun-dif, level_list))), '/', len(level_list))