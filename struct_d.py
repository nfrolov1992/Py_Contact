import func_ab

class Ab:
	def __init__(self, dict_contact, val_contact=None):
		self.dict_contact = dict_contact
		self.val_contact = val_contact

	def use_val_contact(self):
		self.val_contact = len(self.dict_contact)

	def use_look_contact(self):
		for x in self.dict_contact:
			y = self.dict_contact[x]
			print(x, " : ", y)
		print("Всего контактов: ", self.val_contact, '\n')
	
	def use_find_contact(self, name):
		try:
			data_contact = self.dict_contact[name]
			print('\n', name, " : ", data_contact, '\n')			
		except KeyError:
			print("\nКонтакт не найден\n")

	def use_add_contact(self, obj_cont):
		self.dict_contact[obj_cont.name] = obj_cont.tel
		print("\nКонтакт успешно добавлен\n")
		
	def use_del_contact(self, name):
		try:
			self.dict_contact.pop(name)
			print("\nКонтакт успешно удален\n")
		except KeyError:
			print("\nКонтакт не найден\n")
	
	def use_change_contact(self, obj_cont):
		self.use_del_contact(obj_cont.name)
		self.use_add_contact(obj_cont)
	

class Contact:
	def __init__(self, name, tel):
		self.name = name
		self.tel = tel