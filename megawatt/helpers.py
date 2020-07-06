def combine(num, words):
    final = []
    if num > 0 and len(words) >= num:
        if num == 1:
            final = final + [[words[0]]]
        else:
            final = final + [[words[0]] +
                    c for c in combine(num - 1, words[1:])]
        final = final + combine(num, words[1:])
    return final

def next_section(num):
    text.append('\n\\newpage')
    text.append('\n# ' + num + '\n\n')

