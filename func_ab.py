import sys

def main_menu():
	use_look = "Просмотр контактов - 1"
	use_add = "Добавить контакт - 2"
	use_change = "Изменить контакт - 3"
	use_del = "Удалить контакт - 4"
	use_find = "Найти контак - 5"
	use_exit = "Выход - 0"


	hello_contact = "\nГлавное меню: КОНТАКТАЫ\n\
	\nВыбирете действие:\n\n	{0}\n	{1}\n	{2}\n	{3}\n	{4}\n	{5}\n".format(use_look, use_add, use_change,
														use_del, use_find, use_exit)

	print(hello_contact)
	try:
		msg_use = int(input("Ввод: ")) # обработать неккоректный ввод
		return msg_use
	except (EOFError, ValueError, KeyboardInterrupt, AttributeError):
		print("\nОтмена операции. Выход\n")
		sys.exit()

def question():
	try:
		answer = int(input("Выбирете действие:\n1 - Перейти в главное меню\n0 - Сохранить и выйти\nВвод: "))
	except (EOFError, ValueError, KeyboardInterrupt, AttributeError):
		print("\nОтмена операции. Выход\n")
		sys.exit()
	if answer == 0:
		return answer
	return main_menu()

def out_red(text):
    print("\033[31m {}" .format(text))
	
def out_yellow(text):
    print("\033[33m {}" .format(text))
