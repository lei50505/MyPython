# -*- coding: utf-8 -*-

from xml.etree import ElementTree
from xml.dom import minidom
import codecs
import os

def u(s):
    if type(s) is not unicode:
        return s.decode(u"UTF-8")
    return s
               
def getDirNames(dirPath):
    dirNames = []
    fileNames = os.listdir(u(dirPath))
    for fileName in fileNames:
        filePath = u(dirPath) + u"\\" + u(fileName)
        if os.path.isdir(filePath):
            dirNames.append(u(fileName))
    return dirNames

def writeFileAllLines(filePath,lines):
    fileOper = codecs.open(u(filePath),u"w",u"UTF-8")
    fileOper.writelines(lines)
    fileOper.close()

def writeFile(filePath,fileStr):
    fileOper = codecs.open(u(filePath),u"w",u"UTF-8")
    fileOper.write(u(fileStr))
    fileOper.close()

def readFile(filePath):
    fileOper = codecs.open(u(filePath),u"rU",u"UTF-8")
    fileStr = fileOper.read()
    fileOper.close()
    return u(fileStr)

def readFileLines(filePath):
    fileLines = []
    fileOper = codecs.open(u(filePath),u"rU",u"UTF-8")
    lines = fileOper.readlines()
    for line in lines:
        uline = u(line.strip())
        fileLines.append(uline)
    fileOper.close()
    return fileLines

def writeFileLines(filePath,lines):
    fileOper = codecs.open(u(filePath),u"w",u"UTF-8")
    for line in lines:
        uline = u(line.strip() + os.linesep)
        fileOper.write(uline)
    fileOper.close()

def create():
    root = ElementTree.Element(u"Root")
    item = ElementTree.SubElement(root, u"Item")
    item.attrib[u"Name"]=u"曹磊"
    tree = ElementTree.ElementTree(root)
    tree.write(u"config.xml",u"UTF-8")

    dom = minidom.parse(u"config.xml")
    fileOper = codecs.open(u"config.xml",u"w",u"UTF-8")
    dom.writexml(fileOper, addindent = u"    " , newl = u"\n" ,encoding = u"UTF-8")
    fileOper.close()
    
    domStr = dom.toprettyxml(indent=u"    ", newl = u"\n",encoding=u"UTF-8")
    writeFile("config.txt",domStr.decode(u"UTF-8"))

def main():
    dirNames = getDirNames(u"dir")
    for event,elem in ElementTree.iterparse(u"config.xml"):
        if event == u"end":
            if elem.tag.decode(u"UTF-8") == u"Item":
                for dirName in dirNames:
                    if dirName == elem.attrib[u"Name"]:
                        print u"OK"
        elem.clear()
    create()
    writeFile(u"cfg.txt",u(os.linesep))

    lines = readFileLines(u"config.txt")
    writeFileLines(u"cfg.xml",lines)
main()
