#!/usr/bin/env python

from parser import DmozParser
from handlers import JSONArrayWriter

parser = DmozParser()
parser.add_handler(JSONArrayWriter('output.json'))
parser.run()
