#!"C:\Python27\python.exe
# -*- coding: utf-8 -*-

import sqlite3
import sys
import os
import cgi
import datetime

if (os.environ['REQUEST_METHOD'] != "POST"):
	connector = sqlite3.connect("test.db");
	now = datetime.datetime.now().replace(microsecond = 0);
	connector.execute("INSERT INTO like VALUES('%s', '%s');" % (now.isoformat(), "false"));
	connector.commit();
	connector.close();
	
	print "Location: /test.html\n\n"
else:
	sys.exit();

