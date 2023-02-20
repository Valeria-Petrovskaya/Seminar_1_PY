ticket_number = input("Введите номер билета: ")
Sum1= int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
Sum2 = int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])
if Sum1 == Sum2:
    print("Yes")
else:
    print("No")