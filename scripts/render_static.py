#!/usr/bin/env python
'''
Simple functionality to try to parse out Gollum-specific idioms and translate them
to Github flavored markdown.  Ultimately this would be used to transform my Gollum wiki
into a static site in a more systematic way.  Right now, there's technically gollum-site,
but that hasn't been updated in over 6 years and I don't trust that it's current.
I'm more confident in pandoc or Jekyll's ability to render HTML from Markdown that is
put together by the functions below.
'''
import re
from os.path import splitext
   
IMG_EXTENSIONS = ['png','gif','jpeg','jpg','jp2','tif','tiff']

def findOneParam(x):
    match = re.match('\[\[([^|\[\]]+)\]\]',x)
    if match:
        return match.group(1)
    else:
        return False   

def findTwoParam(x):
    match = re.match('\[\[([^|\[\]]+)\|([^|\[\]]+)\]\]',x)
    if match:
        return match.group(1,2)
    else:
        return False

def isLink(param, pageList):
    # External named link
    if param.startswith('http'):
        return True
    # Internal named link, pageList contains extensions
    elif param in pageList:
        return True
    # Internal named link, version of pageList with no extensions
    elif param in [splitext(x)[0] for x in pageList ]:
        return True
    else:
        return False
    
def isImage(param1):
    x = splitext(param1)
    if len(x) == 2:
        if x[1].strip('.') in IMG_EXTENSIONS:
            return True
        else:
            return False
    else:
        return False

def isToc(param1):
    if param1.strip() == '_TOC_':
        return True
    else:
        return False

def main():
    pageList = ['Scientist-Computer-Symbiosis-Obstacles.md','Text-Editors.md']
    testCases = ['[[Scientist-Computer-Symbiosis-Obstacles.md]]','[[Text-Editors]]','[[Obstacles|Scientist-Computer-Symbiosis-Obstacles.md]]','[[Editors|Text-Editors]]','[[https://zombo.com]]','[[Zombocom|https://zombo.com]]','[[https://libjpel.so/images/pellman.jpg]]','[[https://libjpel.so/images/pellman.jpg|alt=text]]','[[_TOC_|levels =3]]','[[_TOC_]]']
    print('Iterating through test cases...')
    print('='*25)
    for testCase in testCases:
        print(testCase)
        oneparamtest = findOneParam(testCase)
        twoparamtest = findTwoParam(testCase)
        linktest = False
        imagetest = False
        toctest = False
        if oneparamtest:
            print('One parameter: %s' % str(oneparamtest))
            linktest = isLink(oneparamtest, pageList)
            imagetest = isImage(oneparamtest)
            toctest = isToc(oneparamtest)
        if twoparamtest:
            print('Two parameters: %s' % str(twoparamtest))
            linktest = isLink(twoparamtest[1], pageList)
            imagetest = isImage(twoparamtest[0])
            toctest = isToc(twoparamtest[0])
        if linktest:
            print("Is link")
        else:
            print("Isn't link")
        if imagetest:
            print("Is image")
        else:
            print("Isn't image")
        if toctest:
            print("Is ToC")
        else:
            print("Isn't ToC")
        print('='*25)
        
if __name__ == '__main__':
    main()
