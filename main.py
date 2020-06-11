import sys
import json
import pickle
import struct_d
import func_ab

FILE = "contact.data"
# загружаем БД
try:
	f = open(FILE, 'rb')
	dict_contact = pickle.load(f)
	print("Загружена структура данных адресной книги ", dict_contact)
	f.close()
except (EOFError, FileNotFoundError):
	dict_contact = {'Nikita' : '89150054263',
					'Nastya' : '89150054263'}
	print("Создана структура данных адресной книги ", dict_contact)

# записываем словарь в объект
obj_ab = struct_d.Ab(dict_contact)
obj_ab.use_val_contact()

# Главное меню. Логика
go_to = func_ab.main_menu()
while True:
	if go_to == 1: # look
		obj_ab.use_look_contact()
	elif go_to == 2: # add
		name = input("Введите имя контакта: ")
		tel = input("Введите телефон контакта: ")
		cont = struct_d.Contact(name, tel)
		obj_ab.use_add_contact(cont)
	elif go_to == 3: # change
		name = input("Введите имя контакта для изменения: ")
		tel = input("Введите телефон контакта для изменения: ")
		cont = struct_d.Contact(name, tel)
		obj_ab.use_change_contact(cont)
	elif go_to == 4: # del
		name = input("Введите имя контакта: ")
		obj_ab.use_del_contact(name)
	elif go_to == 5: # find
		name = input("Введите имя контакта: ")
		obj_ab.use_find_contact(name)
	elif go_to == 0: # save and exit
		f = open(FILE, 'wb')
		pickle.dump(obj_ab.dict_contact, f)
		f.close()
		print("\nИзменения сохранены. Выход\n")
		sys.exit()
	go_to = func_ab.question()