# function: tag, what, return type, parameter_count, parameter_types
# procedure: same as function except return type
# variable: tag, what, type, value
# types: tag, what, width

# If record needs to be copied, rec a = rec b, copy all variables in both one by one. Record variables
# are stored as <record_name>.<var_name>

import csv

Z = {}
U = []

class SymbolTable:

	def __init__ (self, parentTable = None):
		self.parentTable = parentTable
		self.beginLine = None; self.endLine = None;
		self.scope = None
		self.neg_offset = 0
		self.pos_offset = 8
		self.act_rec = {'return_addr': 8}
		self.width_dict = {'Integer': 4, 'Float': 8, 'Char': 1}
		if parentTable == None :
			self.table = {'Integer': {'tag': 'Integer', 'what': 'type', 'width': 4},
						'Float': {'tag': 'Float', 'what': 'type', 'width': 8},
						'Char': {'tag': 'Char', 'what': 'type', 'width': 1},
						'print_int': {'tag': 'print_int', 'what': 'io_function'},
						'scan_int' : {'tag': 'scan_int', 'what': 'io_function'},
						'print_float': {'tag': 'print_float', 'what': 'io_function'},
						'scan_float' : {'tag': 'scan_float', 'what': 'io_function'},
						'print_char': {'tag': 'print_char', 'what': 'io_function'},
						'scan_char' : {'tag': 'scan_char', 'what': 'io_function'},
						'sin' : {'tag': 'sin', 'what': 'default_function'},
						'cos' : {'tag': 'cos', 'what': 'default_function'},
						'tan' : {'tag': 'tan', 'what': 'default_function'},
						'exp' : {'tag': 'exp', 'what': 'default_function'},
						'log' : {'tag': 'log', 'what': 'default_function'},
						'Ada.Text_IO' : {'tag': 'Ada.Text_IO', 'what': 'default_lib'},
						'Ada.Gnat_IO' : {'tag': 'Ada.Gnat_IO', 'what': 'default_lib'},
						'Ada.Integer_Text_IO': {'tag': 'Ada.Integer_Text_IO', 'what': 'default_lib'}	}
		else:
			self.table = {}

	def insert (self, var, attr_dict):
		if var in self.table:
			print ('ERROR: Entity already exists')
			return False
		self.table[var] = attr_dict
		if attr_dict['what'] == 'var':
			width = self.width_dict[attr_dict['type']]
			self.neg_offset += width
			self.act_rec[var] = -self.neg_offset
		elif attr_dict['what'] == 'array':
			width = self.width_dict[attr_dict['type']]
			self.neg_offset += attr_dict['width']
			self.act_rec[var] = -self.neg_offset
		elif attr_dict['what'] == 'record_type':
			for k,v in attr_dict.items():
				if k not in ['what','tag']:
					rec_ele = var + '.' + v['tag']
					width = self.width_dict[attr_dict['type']]
					self.neg_offset += width
					self.act_rec[rec_ele] = -self.neg_offset
		return True

	def update (self, var, attr, val):
		currTable = self
		while (currTable != None):
			if var not in currTable.table:
				currTable = currTable.parentTable
			else:
				currTable.table[var][attr] = val
				return True
		print ('ERROR: Update. Entity does not exist.')
		return False

	def getAttrVal (self, var, attr):
		currTable = self
		while (currTable != None):
			if var not in currTable.table:
				currTable = currTable.parentTable
			else:
				return currTable.table[var][attr]
		print ('ERROR: GetAttrVal.', var, 'does not exist.')
		return None

	def getAttrDict (self, var):
		currTable = self
		while (currTable != None):
			if var not in currTable.table:
				currTable = currTable.parentTable
			else:
				return currTable.table[var]
		print ('ERROR: GetAttrDict.', var, 'does not exist.')
		return None

	def getWidth (self, dtype):
		currTable = self
		while (currTable != None):
			for k in currTable.table:
				if (currTable.table[k]['what'] == 'type' and currTable.table[k]['tag'] == dtype):
					return (currTable.table[k]['width'])
			currTable = currTable.parentTable
		return (None)

	def doesExist (self, var):
		currTable = self
		while (currTable != None):
			if (var in currTable.table):
				return True
			else:
				currTable = currTable.parentTable
		return False

# parameter pass by reference may need to be handled differently

	def insert_param (self, var, attr_dict):
		if var in self.table:
			print ('ERROR: Entity already exists')
			return False
		self.table[var] = attr_dict
		if attr_dict['what'] == 'var':
			width = 4 if attr_dict['type'] == 'Integer' else 8
			self.pos_offset += width
			self.act_rec[var] = self.pos_offset
		elif attr_dict['what'] == 'record_type':
			for k,v in attr_dict.items():
				if k not in ['what','tag']:
					rec_ele = var + '.' + v['tag']
					width = 4 if v['type'] == 'Integer' else 8
					self.pos_offset += width
					self.act_rec[rec_ele] = self.pos_offset

	def beginScope (self, scope):
		newTable = SymbolTable(self)
		newTable.scope = scope
		return (newTable)

	def endScope (self):
		# print (self.scope, self.beginLine, self.endLine)
		return (self.parentTable)

	def printTable (self):
		for k in self.table:
			print (self.table[k])

	def printActRec (self):
		print ('######### ' + self.scope + ' #########')
		for k in self.act_rec:
			print (k, self.act_rec[k])
		print ('###########################\n')