import keyboard
import mouse
from time import sleep
from datetime import datetime

# Вывод статистики
statistics = False
# Для старта скрипта 
status = False
# Подсчет количества нажатий на правую кнопку мыши
count = 0
# Служебная переменная
alt_press = False
while True:
	# Снижение нагрузки на процессор
	sleep(0.01)

	# Запуск скрипта
	if status:
		if statistics:
			time_1 = datetime.today()
		
		keyboard.press("shift")
		mouse.click("right")
		if statistics:
			count += 1
		keyboard.release("shift")
		sleep(0.25)
		keyboard.press("s")
		sleep(0.18)

		# Слежебная переменная для скрипта (Отвечает за разное время между интервалами)
		simple_smart = False

		# Основной цикл
		while True:
			keyboard.press("shift")
			sleep(0.25)
			mouse.click("right")
			if statistics:
				count += 1
			if keyboard.is_pressed("Alt"):
				
				# Статистика
				if statistics:
					print("Статистика")
					print("Time:", datetime.today() - time_1)
					print("Количество поставленных блоков ->", count); count = 0

				keyboard.release("s")
				keyboard.release("shift")
				break
			keyboard.release("shift")

			if simple_smart:
				sleep(0.145)
				simple_smart = False
			else:
				sleep(0.18)
				simple_smart = True
		status = False

	# Разрешаем запустить скрипт еще раз если кнопка Alt была отпущена
	if not keyboard.is_pressed("Alt"):
		alt_press = True

	# Запуск скрипта
	if keyboard.is_pressed("Alt") and alt_press:
		alt_press = False
		status = True
		count = 0

	# Выход
	if keyboard.is_pressed("0"):
		# Очистка консоли
		import msvcrt
		while msvcrt.kbhit():
			msvcrt.getch()
		import os; os.system("cls")
		exit()
