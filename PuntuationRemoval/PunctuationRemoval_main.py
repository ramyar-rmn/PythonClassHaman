punctuations = ('.', ',', '"', "'", '[', "]", "{", "}", ":", ";",
                "?", "!", ">", "<", "/", "*", "=", "#", ' ', '(',
                ')', '\n', "\\",
                )

a = ''', 'i'       'i' Van Rossum was born and raised in the Netherlands, where he received a master's degree in\
 "mathematics and computer science" from the University of Amsterdam in 1982. He has a brother, Just van Rossum, \
 who is a type designer and programmer who designed the typeface used in the \"Python Powered\" logo.'''
a = """salam   '''  'salam salam' 'salam' ''salam sala'm sala''m"""

li = a.split(' ')
i = 0
while i < len(li):
    if len(li[i]) == 0:
        del li[i]
        i -= 1
    elif len(li[i]) == 1 and li[i] in punctuations:
        del li[i]
        i -= 1
    else:
        while len(li[i]) != 0:
            if li[i][0] in punctuations:
                li[i] = li[i][1:]
            elif li[i][-1] in punctuations:
                li[i] = li[i][:-1]
            else:
                break
        else:
            del li[i]
            i -= 1
    i += 1
print(li)
