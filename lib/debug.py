#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.category import Category

import ipdb

Category.drop_table()
Category.create_table()

ipdb.set_trace()