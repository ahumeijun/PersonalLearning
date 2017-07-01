# -*- coding: utf-8 -*-
#!/usr/bin/env python

import dateutil.parser
import datetime
import sys

try:
    query = sys.argv[1]
    date = dateutil.parser.parse(query)
    print(int(date.timestamp()))
finally:
    pass
