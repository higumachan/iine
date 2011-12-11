#!"C:\Python27\python.exe
# -*- coding: utf-8 -*-

import sqlite3
import sys
import os
import cgi
import datetime
import json

if (0):
	sys.exit();
else:
	result = {"like_count":0};
	connector = sqlite3.connect("test.db");
	cursor = connector.cursor();
	cursor.execute("SELECT COUNT(see_flag) FROM like WHERE see_flag='false';");
	connector.execute("UPDATE like SET see_flag='true' WHERE see_flag='false'");
	connector.commit();
	result["like_count"] = cursor.fetchone()[0];
	
	print "Content-Type: text/html; charset=utf-8"
	print "";
	print json.dumps(result);
	
	
	cursor.close();
	connector.close();

