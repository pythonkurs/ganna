import os

class repo_dir(object):
	def __init__(self, path):
		self.current_path = os.getcwd()
		self.working_path = path
		
	def __enter__(self):
		os.chdir(self.working_path)
		
	def __exit__(self, *_):
		os.chdir(self.current_path)

class CourseRepo(object):
	
	def __init__(self, surname):
		self.required=[]
		self.surname = surname
		
	@property
	def surname(self):
		return self._surname
	
	@surname.setter	
	def surname(self,value):
		self.required.append(".git")
		self.required.append("setup.py")
		self.required.append("README.txt")
		self.required.append("scripts/getting_data.py")
		self.required.append("scripts/check_repo.py")
		self.required.append(value + "/__init__.py")
		self.required.append(value + "/session3.py")
		self._surname = value
		
	def check(self):
		for item in self.required:
			if not os.path.exists(item):
				return False
			return True