#!/usr/bin/python3
"""text identation funct"""


def text_indentation(text):
    """function"""
    st = ""
    if type(text) != str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == " " and text[i - 1] == " " and i != 0:
            pass
        elif text[i] in {'.', '?', ':'}:
            st += text[i] + "\n\n"
        else:
            st += text[i]
    for i in range(len(st)):
        if st[i] == " " and st[i - 1] == "\n" and i != 0:
            pass
        else:
            print(st[i], end="")
