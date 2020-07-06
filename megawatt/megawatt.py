from . import helpers

__author__ = 'nick montfort'
__license__ = 'isc'
__version__ = '1.0'

#all of these could be in their own 'constants' file, since they don't change. how would you organize that file?

spelled_out = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty'
}

voices = ['sang', 'cried', 'stated', 'murmured', 'babbled', 'chattered',
          'ranted', 'whispered']
understood = ['all', 'most', 'much', 'half', 'little', 'less', 'bits',
              'nothing']
preface = ', and sometimes they '


def write_chapter_1():
    # try putting these outside of this function to see what happens - why do these need to be in the function, when the other variables don't?
    text = []
    para = ''
    for num in range(len(voices)):
        for word_list in helpers.combine(num + 1, voices):
            para = para + preface + ' and '.join(word_list)
            if len(word_list) == 1:
                para = para + ' only'
    para = ('Watt heard voices. Now these voices,' + para[5:] +
            ', all together, at the same time, as now, to mention ' +
            'only these ' + spelled_out[len(voices)] + ' kinds of voices, for ' +
            'there were others. And sometimes Watt understood ' +
            ', and sometimes he understood '.join(understood) + ', as now.')
    text.append(para)
    return ' '.join(text)



