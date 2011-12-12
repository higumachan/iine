#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import sys
import os
import cgi
import datetime
import json

if (1):
	connector = sqlite3.connect("test.db");
	form = cgi.FieldStorage();
	#2010-12-06T00:00:00&end=2010-12-06T23:00:00
	try:
		start = form['start'].value;
		end = form['end'].value;
	except:
		start = '2011-12-06T00:00:00';
		end = '2011-12-06T23:00:00';
	cursor = connector.cursor();
	cursor.execute("SELECT COUNT(time), time FROM like WHERE time > '%s' AND time < '%s' GROUP BY time;" % (start, end));
	rows = cursor.fetchall();
	s = datetime.datetime.strptime(start, "%Y-%m-%dT%H:%M:%S");
	e = datetime.datetime.strptime(end, "%Y-%m-%dT%H:%M:%S");
	
	result = {"chart_data":[]};
	dic = {};
	for row in rows:
		delta = datetime.datetime.strptime(row[1], "%Y-%m-%dT%H:%M:%S") - s; 
		dic[delta.seconds] = row[0];
	for i in range((e - s).seconds):
		if (dic.has_key(i) == True):
			result["chart_data"].append((i, dic[i]));
		else:
			result["chart_data"].append((i, 0));
		
	print "Content-Type: text/html; charset=utf-8"
	print "";
	print json.dumps(result);

