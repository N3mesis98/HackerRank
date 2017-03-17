#!/usr/bin/python3

import re
print(re.search("^(?![0-9]*([0-9])([0-9])\\1\\2)[1-9][0-9]{5}$", input()) != None)
