#!/usr/bin/env python3
# encoding: utf-8

import urllib.request

agent = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}

def convertUnicodeToHTMLEsc(text):
    htmlEsc = str(text.encode()).replace("b\'\\x", "%").replace("\\x", "%").replace("\'", '')
    return htmlEsc

def translateFromUnicode(to_translate, to_language="auto", language="auto"):
    htmlEsc = convertUnicodeToHTMLEsc(to_translate)
    translation = translate(htmlEsc, to_language, language)
    return (translation)

def translate(to_translate, to_langage="auto", langage="auto"):
    """
    Return the translation using google translate
    you must shortcut the langage you define (French = fr, English = en, Spanish = es, etc...)
    if you don't define anything it will detect it or use english by default
    Example:
    print(translate("salut tu vas bien?", "en"))
    hello you alright?
    """
    before_trans = 'class="t0">'
    link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (to_langage, langage, to_translate.replace(" ", "+"))
    request = urllib.request.Request(link, headers=agent)
    page = urllib.request.urlopen(request).read().decode("utf-8")
    result = page[page.find(before_trans)+len(before_trans):]
    result = result.split("<")[0]
    return(result)


if __name__ == '__main__':
    to_translate = 'Hola como estas?'
    print("%s >> %s" % (to_translate, translate(to_translate)))
    print("%s >> %s" % (to_translate, translate(to_translate, 'fr')))
    to_translate = 'نمر'
    print(translateFromUnicode('نمر', "en", "ar"))
    #should print Hola como estas >> Hello how are you
    #and Hola como estas? >> Bonjour comment allez-vous?
