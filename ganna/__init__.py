#!/usr/bin/env python

def ganna_outage ():
	import requests
	import untangle
	"Read xml data"
	r = requests.get("http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml")
	"Assign text to object"
	r_f = r.text
	"Read xml object"
	r_f_u = untangle.parse(r_f)
	"Check elements"
	r_f_u.get_elements()
	outages = r_f_u.NYCOutages.outage
	print 'THERE ARE', len(outages), 'OUTAGES'
	print 'THIS ARE THE OUTAGES REASONS:'
	i=0
	for outage in r_f_u.NYCOutages.outage:
		data = outage.reason.cdata
		print data
		if data == 'REPAIR':
			i=1+i
	exp = (i/float(len(outages)))*100	
	print 'THIS MEANS THAT', i, '/', len(outages),'=',("%.1f" % exp) ,'%','IS REPAIRING'
	return
