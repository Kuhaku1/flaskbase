# -*- coding:utf-8 -*-

import os
import sys

try:
    os.system("npm install")
    print("================================")
    print("=    happy coding.             =")
    print("================================")
    sys.exit(0)
except Exception as e:
    sys.exit(1)
