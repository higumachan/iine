#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import sys
import os
import cgi
import datetime

if (1):
	connector = sqlite3.connect("test.db");
	now = datetime.datetime.now().replace(microsecond = 0);
	connector.execute("INSERT INTO like VALUES('%s', '%s');" % (now.isoformat(), "false"));
	connector.commit();
	connector.close();
	
	print "Content-Type: text/html; charset=utf-8"
	print "";
	print """
    <form action="/cgi-bin/test.py" method="POST">
        <input type="submit" value="like"/>
    </form>
    """
else:
	sys.exit();

