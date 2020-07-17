import docx
import platform
import os
import os.path
from os import path

def getText(filename):
    """Gets thje text from the word document

    Arguments:
        filename {string} -- [the filename of the word document]

    Returns:
        [string] -- [returns the text from the document]
    """
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def printTable(myDict, colList=None):
    """Prints a table from dictionary value\
        I only used for error checking

    Arguments:
        myDict {dict} -- [the dictiopnary value]

    Keyword Arguments:
        colList {string} -- [the column to specify for printing] (default: {None})
    """

    if not colList: 
        colList = list(myDict[0].keys() if myDict else [])
        myList = [colList] # 1st row = header
        for item in myDict: 
            myList.append([str(item[col] if item[col] is not None else '') for col in colList])
            colSize = [max(map(len,col)) for col in zip(*myList)]
            formatStr = ' | '.join(["{{:<{}}}".format(i) for i in colSize])
            myList.insert(1, ['-' * i for i in colSize]) 
            for item in myList: 
                print(formatStr.format(*item))