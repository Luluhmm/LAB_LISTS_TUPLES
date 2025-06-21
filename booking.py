#Luluh Almogbil 
'''
# LAB_LISTS_TUPLES

## Cinema Booking Program
Create A small cinema program that uses a basic system to track **booked seats** for each show. Each booked seat is represented as a **tuple** of the form `(row_number, seat_number)`, and the full booking list is a **list of these tuples**.

---

### **Description**

You are given a list of booked seats for a movie show. Each seat is represented as a tuple `(row, seat)` where:

* `row` is an integer from 1 to 10
* `seat` is an integer from 1 to 20

Example:

```python
booked_seats = [(1, 5), (1, 6), (2, 10), (3, 7), (4, 15)]
```

Write a program that performs the following tasks:

---

### **Tasks**

1. **Display all booked seats** in the format:

   ```
   Row 1, Seat 5  
   Row 1, Seat 6  
   ...
   ```

2. **Check availability:** Ask the user to enter a seat (e.g., row 2, seat 10), and tell them whether the seat is **booked** or **available**.

3. **Add a booking:** ask the user to enter the seat, row . if available, add it to the `booked_seats` list. else display a relevant message.

4. **Cancel a booking:** Ask the user to enter a row & a seat to cancel. If it's in the list, remove it.

5. **Print all booked seats, sorted by row and then seat**.

6. **Calculate and display**:

   * Total number of booked seats
   * Number of seats booked per row (use a list of counts for each row index 0–9)

### Note:
The program when run should run and displays a menu that asks the user what he/she wants to do based on the above tasks, and only exits if the user types in "exit".

---

### **Constraints**

* Use only **lists and tuples**.
'''

booked_seats = [(1, 5), (1, 6), (2, 10), (3, 7), (4, 15)] #[list > mutable],(tuple > immuatble)

#1
def print_booked():
    '''
    This function will display all booked seats in via riyadh cinemas'
    '''
    print("Booked seats: ")
    for row,seat in booked_seats:
        print(f"Row {row}, seat {seat}")
    print("Thank you!")

#2
def check_av():
    print("Please enter the row and seat numbers so I can check availability: ")
    row = int(input("Please enter row number from (1-10)"))# i faced a probelm here where i needed to conver the input into integer beacause "5" will be entered not 5 and they are not the same
    seat = int(input("Please enter seat number from (1-20)"))

    if (row,seat) in booked_seats:
        print("Seat is booked")
    else:
        print("Seat is available")

#3
def add_booking():
    print("Please enter the row and seat wanted to book it for you : ")

    while True:
           row = int(input("Please enter row number from (1-10)"))
           seat = int(input("Please enter seat number from (1-20)"))
           if (row,seat) in booked_seats:
               print("Seat is booked, please enter another seat number")
           else:
               print(f"Seat {row},{seat} is available for booking , we will book it for you!")
               booked_seats.append((row,seat))
               print("booking went successfully! this is all booked seats updated:")
               for r,s in booked_seats:
                   print(f"Row {r},Seat {s}")
               print("Thank you")
               break
               
               
#4
def cancel():
    print("Please enter the row and seat numbers to cancel booking: ")
    row = int(input("Please enter row number from (1-10) to cancel "))# i faced a probelm here where i needed to conver the input into integer beacause "5" will be entered not 5 and they are not the same
    seat = int(input("Please enter seat number from (1-20) to cancel "))

    if (row,seat) in booked_seats:
        print(f"Seat that will be canceled is : {row}, {seat}")#remove it if it is in the list
        booked_seats.remove((row,seat))
        print("booking Cancelled successfully!\n These are all booked seats after cancelation: ")
        for r,s in booked_seats:
            print(f"Row {r},Seat {s}")
        print("Thank you!")
  
    else:
        print("This seat is NOT booked")#if it not in the list say it is not booked

#5
def sorted_booking():
    sorted_seats = sorted(booked_seats)#built in function 
    print("Sorted Bookings: ")
    for row,seat in sorted_seats:
        print(f"Row {row}, Seat {seat}")

#6
def summary():
    print(f"Total number of booked seats: {len(booked_seats)}")
    rowCount = [0]*10 #>[0, 0, 0 ,0 ....]
    for row, _ in booked_seats:#_ is any seat number
        rowCount[row-1] += 1# index 0 = row 1 do if there is booking in first row > index0 +1 , increase the roucounter to count how many seats booked in each row
        #[2, 1, 0 ,0 ....] in row 1 there is 2 seats and so on
    for i, count in enumerate(rowCount):# i is index and count is the value in the index
        print(f"Row {i+1} : {count} seats booked")


    

# Color codes
PINK = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

print(f"{PINK}{BOLD} Welcome to our Via Riyadh Cinema Booking System!{RESET}")
print(f"{PINK}We are excited to help you reserve your perfect seat today.{RESET}")
print(f"{PINK}To continue, please type '{BOLD}(yes/no){RESET}{PINK}' to open the main menu.{RESET}")

display = input("> ").strip().lower()#.strip().lower() #strip will remove any unnecessary spaces and lower will lower the capital letters enterd from the user to avoid any exceptions



if display == "yes":
    while True:
        print("----Welcome to our MAIN MENU----")
        print("1. Show all booked seats")
        print("2. check seat availability")
        print("3. Add a booking")
        print("4. Cancel a booking")
        print("5. Show sorted booked seats")
        print("6. Booking summary")
        print("Please type 'exit' to quit the menu")

        choice = input("Please select an option from the displayed menu : ").strip().lower()
        match choice:
            case "1":#numbers will be seen by pvm as a string
                print(print_booked.__doc__)
                print_booked()
            case "2":  
                check_av()
            case "3":
                add_booking()
            case "4":
                cancel()
            case "5":
                sorted_booking()
            case "6":
                summary()
            case "exit":
                print(f"{PINK}{BOLD}Thank you for using Via Riyadh Cinema Booking. We hope to see you soon, Goodbye!{RESET}")
                break
            case _:
                print("Invalid option")
else:
    print(f"{PINK}{BOLD}Goodbye! inshallah we will see you soon ;){RESET}")

    