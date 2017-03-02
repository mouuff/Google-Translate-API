#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from .core import translate
import sys

USAGE = ("""Name: mou_translator
Usage:
$ mou_translator text_to_translate to_lang from_lang

from_lang is optional

Example:
$ mou_translator "bonjour" en
Hello
""")


def main():
    if (len(sys.argv) < 3):
        print(USAGE)
        return (1)
    text = sys.argv[1]
    dest = sys.argv[2]
    if (len(sys.argv) > 3):
        src = sys.argv[3]
    else:
        src = "auto"
    print(translate(text, dest, src))
    return (0)

if __name__ == '__main__':
    main()
