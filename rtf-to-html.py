#!/usr/bin/env python
# -*-coding:utf-8-*-
# encoding:utf-8
from pyth.plugins.rtf15.reader import Rtf15Reader
from pyth.plugins.plaintext.writer import PlaintextWriter

try:
    doc = Rtf15Reader.read(open('test.rtf'))
    output = PlaintextWriter.write(doc).getvalue()
    output = output.replace("\r", "<br>").replace("\n", "<br>").replace("\t", " ").replace(chr(10), '<br />')
    f = open("output.html", mode="w")
    f.write(output)
    f.close()
except ValueError:
    print("Error: " + i['ID'])
    print(ValueError)
