
import AppClass_sm


class AppClass:
	c: str
	substr = ''
	liststr = []
	set = set()
	dict = {}
	def __init__(self):
		self._fsm = AppClass_sm.AppClass_sm(self)
		self._is_acceptable = False
		self.aim = ""

	def CheckString(self, string):
		self._is_acceptable = False
		substr = ""
		self._fsm.enterStartState()
		for self.c in string:
			if self.c == ' ':
				self._fsm.Space()
			elif self.c == ':':
				self._fsm.Colon()
			elif (self.c >= '0') and (self.c <= '9'):
				self._fsm.Digit()
			elif(self.c == '.') or (self.c == '_') or (self.c <= 'Z') and (self.c >= 'A') or (self.c <= 'z') and (self.c >= 'a'):
				self._fsm.Letter()
			else:
				self._fsm.Unknown()
		self._fsm.EOS()
		# if InTheList(strList, substr):
		# 	self._is_acceptable = False
		# 	return self._is_acceptable
		# if self._is_acceptable:
		# 	self.aim = strList[0]
		return self._is_acceptable
	def Acceptable(self):
		self._is_acceptable = True

	def Unacceptable(self):
		self._is_acceptable = False

	def fillSetAndDict(self):
		for i in self.liststr:
			if i == self.liststr[0]:
				self.set.add(i)
			else:
				if self.dict.get(i) == None:
					self.dict[i] = 1
				else:
					self.dict[i] += 1


	def addToList(self):
		self.liststr.append(self.substr)

	def clearApp(self):
		self.clearSubStr()
		self.liststr.clear()

	def clearSubStr(self):
		self.substr = ""

	def addSubStr(self):
		self.substr += self.c


	def InTheList(self):
		for i in self.liststr:
			if i == self.substr:
				return False
		return True
