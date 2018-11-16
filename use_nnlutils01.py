#!/usr/bin/env python
import sys
from nnl.tech import nnlutils

nnlutils.spam()
nnlutils.ham()

# nnlutils._toast()

print(sys.prefix)

# CURR_DIR + $PYTHONPATH + BUILTIN

for path in sys.path:
    print(path)
