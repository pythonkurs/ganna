#!/usr/bin/env python

import os
import sys

from ganna.session3 import CourseRepo, repo_dir

CHECK='FAIL'

dir=sys.argv[1]
surname=os.path.basename(dir)

with repo_dir(dir):
	repo=CourseRepo(surname)
	if repo.check()==True:
		CHECK='PASS'
		
	print CHECK + ' this is the surname: ' + surname + ' and this is the directory: ' + dir
	
	