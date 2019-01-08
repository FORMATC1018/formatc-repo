number_room = int(input("Введите номер комнаты "))
count=1
first_room=1
number_first_rooms=[1]
while first_room<number_room:
	for num in range(count):
		if first_room<number_room:
			first_room += count
			number_first_rooms.append(first_room)
		else:
			break
	count+=1
floor = len(number_first_rooms) - 1
print ("Этаж - ", floor)
pos = number_room - number_first_rooms[floor-1]+1
print ("Позиция на этаже - ", pos)

