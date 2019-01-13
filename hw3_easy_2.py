def lucky_ticket(ticket_number):
	ticket_number_1 = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
	ticket_number_2 = int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])
	return (ticket_number_1==ticket_number_2)


ticket_number = input("Введите шестизначный номер билета - ")
if len(ticket_number) == 6 :
	print(lucky_ticket(ticket_number))
else:
	print("Введенный номер некорректен")