# import all the needed things
import json
import jsonpickle

def createSeating():
    """
        Reset all seatings and purge all purchases
    """
    n_row = 20
    n_col = [chr(i) for i in range(ord("A"), ord("Z")+1)]
    seating=[]
    price=0
    frontSeat=range(5)
    middleSeat=range(5,11)
    backSeat=range(11,20)
    seat_type=""
    for r in range(n_row):
        for c in n_col:    
            if r in frontSeat:
                price=80
                seat_type="Front"
            elif r in middleSeat:
                price=50
                seat_type="Middle"
            elif r in backSeat:
                price=25
                seat_type="Back"
            seating.append({"col":c, "row":r, "Name":"", "Email":"", "Seat Type":seat_type, "Price":price, "Available":"."})        
    saveJson(seating, "seating.json")
   
    #purge receipt.json
    receipt=[]
    saveJson(receipt,"receipt.json")
   
    return seating

def readJson(filename):
    """
        Read json file, then return an object
    """
    try:
        seating_file = open(filename, "r")
    except IOError:
        #print("Error: File " + filename + " does not appear to exist.")
        return []

    # read the file
    file_data = seating_file.read()

    # close the file
    seating_file.close()

    # decode json into an object
    seating=jsonpickle.decode(file_data)
   
    return seating

def saveJson(seating, filename):
    """
        Receive an object and write to filename with json format
    """
           
    with open(filename , "w") as write:
        json.dump(seating, write, indent=4)
   
    try:
        seating_file = open(filename, "r")
    except IOError:
        print("Error: File " + filename + " does not appear to exist.")
        return -1    
      
def printSeating(seating):
    """
        Print out seatings row, column, type, price, available or not
    """
    n_row = 20
    n_col = 26
   
    #create array ["A", ..., "Z"] for seatings column
    alpha = [chr(i) for i in range(ord("A"), ord("Z")+1)]
   
    # range of seats
    frontSeat=range(5)
    middleSeat=range(5,11)
    backSeat=range(11,20)  
   
    # print seats
    print("-"*77)
    print(" "*35+"Seating")
    print("-"*77)

    seatno=0
    prt_head=" \t"

    # prints the first row with the information of the colomn letter
    for i in alpha:
        prt_head+=i + " "
    prt_head += "\tType\tPrice"
    print(prt_head)  
    print()

    # prints each row after the first row 
    for r in range(n_row):
        prt_col=f"{r}\t"
        for c in range(n_col):
            prt_col += seating[seatno]["Available"] + " "
            seatno+=1
        prt_tail=""

        # depending on seat row prints section and cost
        if r in frontSeat:
            prt_tail="\tfront\t$80"

        elif r in middleSeat:
            prt_tail="\tmiddle\t$50"

        elif r in backSeat:
            prt_tail="\tback\t$25"

        prt_col += prt_tail
        print(prt_col)    
    print()

def socialDistancePlacer():
    """
    places the "e" around the seats 
    """
    if ord("a") == ord(start_col):
        for k in seating:
            if (k["row"] == end_row) and (k["col"].lower() == chr(ord(end_col)+1)):
                k["Available"] = "e"
            elif (k["row"] == end_row+1) and (k["col"].lower() == chr(ord(end_col)+1)):
                k["Available"] = "e"
            elif (k["row"] == end_row-1) and (k["col"].lower() == chr(ord(end_col)+1)):
                k["Available"] = "e"
            elif (k["row"] == end_row) and (k["col"].lower() == chr(ord(end_col)+2)):
                k["Available"] = "e"
            elif (k["row"] == end_row+1) and (k["col"].lower() == chr(ord(end_col)+2)):
                k["Available"] = "e"
            elif (k["row"] == end_row-1) and (k["col"].lower() == chr(ord(end_col)+2)):
                k["Available"] = "e"

    if ord("z") == ord(end_col):
        for k in seating:
            if (k["row"] == start_row) and ((k["col"].lower()) == chr(ord(start_col)-1)):
                k["Available"] = "e"
            elif (k["row"] == start_row+1) and ((k["col"].lower()) == chr(ord(start_col)-1)):
                k["Available"] = "e"
            elif (k["row"] == start_row-1) and ((k["col"].lower()) == chr(ord(start_col)-1)):
                k["Available"] = "e"
            elif (k["row"] == start_row) and ((k["col"].lower()) == chr(ord(start_col)-2)):
                k["Available"] = "e"
            elif (k["row"] == start_row+1) and ((k["col"].lower()) == chr(ord(start_col)-2)):
                k["Available"] = "e"
            elif (k["row"] == start_row-1) and ((k["col"].lower()) == chr(ord(start_col)-2)):
                k["Available"] = "e"

    if ord("b") == ord(start_col):
        for k in seating:    
            if (k["row"] == start_row) and (k["col"].lower() == "a"):
                k["Available"] = "e"
            elif (k["row"] == start_row+1) and (k["col"].lower() == "a"):
                k["Available"] = "e"
            elif (k["row"] == start_row-1) and (k["col"].lower() == "a"):
                k["Available"] = "e"
            elif (k["row"] == end_row) and (chr(ord(k["col"].lower())+1) == chr(ord(end_col)+1)):
                k["Available"] = "e"
            elif (k["row"] == end_row+1) and (chr(ord(k["col"].lower())+1) == chr(ord(end_col)+1)):
                k["Available"] = "e"
            elif (k["row"] == end_row-1) and (chr(ord(k["col"].lower())+1) == chr(ord(end_col)+1)):
                k["Available"] = "e"
            elif (k["row"] == end_row) and (chr(ord(k["col"].lower())+1) == chr(ord(end_col)+2)):
                k["Available"] = "e"
            elif (k["row"] == end_row+1) and (chr(ord(k["col"].lower())+1) == chr(ord(end_col)+2)):
                k["Available"] = "e"
            elif (k["row"] == end_row-1) and (chr(ord(k["col"].lower())+1) == chr(ord(end_col)+2)):
                k["Available"] = "e"
        
    if ord("y") == ord(end_col):
        for k in seating:    
            if (k["row"] == end_row) and (k["col"].lower() == "z"):
                k["Available"] = "e"
            elif (k["row"] == end_row+1) and (k["col"].lower() == "z"):
                k["Available"] = "e"
            elif (k["row"] == end_row-1) and (k["col"].lower() == "z"):
                k["Available"] = "e"
            elif (k["row"] == start_row) and (k["col"].lower() == chr(ord(start_col)-1)):
                k["Available"] = "e"
            elif (k["row"] == start_row+1) and (k["col"].lower() == chr(ord(start_col)-1)):
                k["Available"] = "e"
            elif (k["row"] == start_row-1) and (k["col"].lower() == chr(ord(start_col)-1)):
                k["Available"] = "e"
            elif (k["row"] == start_row) and (k["col"].lower() == chr(ord(start_col)-2)):
                k["Available"] = "e"
            elif (k["row"] == start_row+1) and (k["col"].lower() == chr(ord(start_col)-2)):
                k["Available"] = "e"
            elif (k["row"] == start_row-1) and (k["col"].lower() == chr(ord(start_col)-2)):
                k["Available"] = "e"

    if (ord("c") <= ord(start_col)) and (ord("x") >= ord(end_col)):
        for k in seating:
            if (k["row"] == start_row) and ((k["col"].lower()) == chr(ord(start_col)-1)):
                k["Available"] = "e"
            elif (k["row"] == start_row+1) and ((k["col"].lower()) == chr(ord(start_col)-1)):
                k["Available"] = "e"
            elif (k["row"] == start_row-1) and ((k["col"].lower()) == chr(ord(start_col)-1)):
                k["Available"] = "e"
            elif (k["row"] == start_row) and ((k["col"].lower()) == chr(ord(start_col)-2)):
                k["Available"] = "e"
            elif (k["row"] == start_row+1) and ((k["col"].lower()) == chr(ord(start_col)-2)):
                k["Available"] = "e"
            elif (k["row"] == start_row-1) and ((k["col"].lower()) == chr(ord(start_col)-2)):
                k["Available"] = "e"
            elif (k["row"] == end_row) and ((k["col"].lower()) == chr(ord(end_col)+1)):
                k["Available"] = "e"
            elif (k["row"] == end_row+1) and ((k["col"].lower()) == chr(ord(end_col)+1)):
                k["Available"] = "e"
            elif (k["row"] == end_row-1) and ((k["col"].lower()) == chr(ord(end_col)+1)):
                k["Available"] = "e"
            elif (k["row"] == end_row) and ((k["col"].lower()) == chr(ord(end_col)+2)):
                k["Available"] = "e"
            elif (k["row"] == end_row+1) and ((k["col"].lower()) == chr(ord(end_col)+2)):
                k["Available"] = "e"
            elif (k["row"] == end_row-1) and ((k["col"].lower()) == chr(ord(end_col)+2)):
                k["Available"] = "e"

def menu():
    """
    prints the menu
    """

    # prints out the title
    print()
    print("-"*77)
    print(" "*26+ "Outdoor Park Concert App")
    print("-"*77)

    # prints out the options
    print("[b] Buy")
    print("[v] View seating")
    print("[s] Search for a customer by name and Display the tickets purchased")
    print("[d] Display all the purchases made and Total income")
    print("[q] quit")
    print("-"*77)

def buySeating():
    """
    function to buy seating
    """
    global start_col, start_row, end_col, end_row, seating
    buy = False
    concert_seat = readJson("seating.json")
    printSeating(concert_seat)
    while (not buy):
        seating = readJson("seating.json")
        num_seats = int(input("How much seats would you like to buy (max 24): "))
        if num_seats > 24:
            print("Max is 24")
        else:
            # logic to get all of the information
            start_seat = input("Enter starting seat number (ex. 15A): ")
            # check if input is correct
            if (0 <= int(start_seat[:-1]) <= 19) and (ord("a") <= ord(start_seat[-1].lower()) <= ord("z")):
                name = input("What is your full name?: ")
                email = input("What is your email?: ")
                print()
                start_row = int(start_seat[:-1])
                start_col = start_seat[-1].lower()
                booked_seats = []
                for i in range(num_seats):
                    # Construct the seat number
                    seat = str(start_row) + chr(ord(start_col) + i)
                    booked_seats.append(seat)

                # prints reciept
                seatLoc, ticketNum, fee, cost, subtotal, tax, total = createReciept(name, email, booked_seats)

                confirm = input("Confirm purchase (y/n)? ")
                if confirm[0:1] == "y":
                    # add reciept into receipt.json
                    rec = readJson("receipt.json")
                    rec.append({"Name": name,
                                "Email": email,
                                "Number of Tickets": ticketNum,
                                "Type": seatLoc,
                                "Seats": booked_seats,
                                "Cost": cost,
                                "Fee": fee,
                                "Subtotal": subtotal,
                                "Tax": tax,
                                "Total": total})
                    saveJson(rec, "receipt.json")
                    # changes available "." to not available "X"
                    # nested loops to cover all the seats
                    ind = 0
                    for i in booked_seats:
                        row = int(booked_seats[ind][:-1])
                        col = booked_seats[ind][-1].lower()
                        for k in seating:
                            if (k["row"] == row) and (k["col"].lower() == col):
                                # print(seating[k]["Available"])
                                k["Available"] = "X"
                        ind += 1

                    # replace "." to cover the social distancing seats
                    last = booked_seats[-1]
                    end_row = int(last[:-1])
                    end_col = str(last[-1].lower())

                    if (start_row >= 1) and (start_row <= 18):
                        # logic to put "e" a row above the "X"
                        ind = 0
                        for i in booked_seats:
                            row = int(booked_seats[ind][:-1]) - 1
                            col = booked_seats[ind][-1].lower()
                            for k in seating:
                                if (k["row"] == row) and (k["col"].lower() == col):
                                    # print(seating[k]["Available"])
                                    k["Available"] = "e"
                            ind += 1
                        # logic to put "e" a row below the "X"
                        ind = 0
                        for i in booked_seats:
                            row = int(booked_seats[ind][:-1]) + 1
                            col = booked_seats[ind][-1].lower()
                            for k in seating:
                                if (k["row"] == row) and (k["col"].lower() == col):
                                    # print(seating[k]["Available"])
                                    k["Available"] = "e"
                            ind += 1

                        socialDistancePlacer()
                    elif start_row >= 1:
                        # to put the "e" above the "X"
                        ind = 0
                        for i in booked_seats:
                            row = int(booked_seats[ind][:-1]) - 1
                            col = booked_seats[ind][-1].lower()
                            for k in seating:
                                if (k["row"] == row) and (k["col"].lower() == col):
                                    k["Available"] = "e"
                            ind += 1
                        
                        socialDistancePlacer()
                    elif start_row <= 18:
                        #  to put the "e" below the "X"
                        ind = 0
                        for i in booked_seats:
                            row = int(booked_seats[ind][:-1]) + 1
                            col = booked_seats[ind][-1].lower()
                            for k in seating:
                                if (k["row"] == row) and (k["col"].lower() == col):
                                    # print(seating[k]["Available"])
                                    k["Available"] = "e"
                            ind += 1
                        socialDistancePlacer()
                    saveJson(seating, "seating.json")
                    buy = True
                else:
                    continue
            else:
                continue
        
def readReciepts():
    """
    gets all the receipts and formats them then prints out total profit"""
    reciepts = readJson("receipt.json")
    profit = 0
    print("-"*55)
    print(" "*20 + "All Receipts")   
    print("-"*55)
    for i in reciepts:
        print("-"*55)
        print(f"Name             : {i["Name"]}")
        print(f"Email            : {i["Email"]}")
        print(f"Number of Tickets: {i["Number of Tickets"]}")
        print(f"Seats            : {i["Type"]}")
        print(f"Cost             : ${i["Cost"]}")
        print(f"Mask Fee         : ${i["Fee"]}")
        print(f"Sub-Total        : ${i["Subtotal"]}")
        print(f"Tax              : ${i["Tax"]}")
        print("-"*55)
        print(f"Total            : ${i["Total"]}")
        print("-"*55) 
        profit += i["Total"]
    print("-"*55)
    print(f"Total Profit generated is ${profit:.2f}")
    print("-"*55)

def createReciept(name, email, seats):
    """
    creates reciept for every purchase and stores into variables
    """
    
    # find location of seats
    if 0 <= int(seats[0][:-1]) <= 4:
        seatLoc = "front"
    elif 5 <= int(seats[0][:-1]) <= 10:
        seatLoc = "middle"
    else:
        seatLoc = "back"

    # get cost of all the seats
    if seatLoc == "front":
        cost = len(seats) * 80
    elif seatLoc == "middle":
        cost = len(seats) * 50
    else:
        cost = len(seats) * 25

    # create variables for the information
    ticketNum = len(seats)
    fee = 5 * ticketNum
    subtotal = cost + fee
    tax = round(subtotal * 0.0725, 2)
    total = subtotal + tax
    # prints out the reciept
    print("-"*55)
    print(" "*20 + "Reciept")
    print("-"*55)
    print("-"*55)
    print(f"Name             : {name}")
    print(f"Email            : {email}")
    print(f"Number of Tickets: {ticketNum}")
    print(f"Seats            : {seats}")
    print(f"Cost             : ${cost}")
    print(f"Mask Fee         : ${fee}")
    print(f"Sub-Total        : ${subtotal}")
    print(f"Tax              : ${tax}")
    print("-"*55)
    print(f"Total            : ${total}")
    print("-"*55)

    # return all the information
    return seatLoc, ticketNum, fee, cost, subtotal, tax, total

def searchName():
    """
    searches through people who bought a ticket for their information
    """
    name = input("What is your name: ").lower()
    receipts = readJson("receipt.json")
    # loop through all the reciepts
    for i in receipts:
        name_in_rec = i["Name"].lower()
        if name_in_rec == name:
            # print out the reciept
            print("-"*55)
            print(" "*20 + f"Receipt for {name.capitalize()}")   
            print("-"*55)
            print("-"*55)
            print(f"Name             : {i["Name"]}")
            print(f"Email            : {i["Email"]}")
            print(f"Number of Tickets: {i["Number of Tickets"]}")
            print(f"Seats            : {i["Type"]}")
            print(f"Cost             : ${i["Cost"]}")
            print(f"Mask Fee         : ${i["Fee"]}")
            print(f"Sub-Total        : ${i["Subtotal"]}")
            print(f"Tax              : ${i["Tax"]}")
            print("-"*55)
            print(f"Total            : ${i["Total"]}")
            print("-"*55) 
        

def main():
    global concert_seats
    # loop until user types q
    user_quit = False
    concert_seats = []
    while (not user_quit):

        # menu
        menu()

        # get first character of input
        user_input = input("Enter a command:")
        lower_input = user_input.lower()
        first_char = lower_input[0:1]

        # menu choices, use a switch-like if-elif control structure
        if first_char.lower() == "q":
            print("Thank you for using Outdoor Park Concert App!")
            user_quit = True

        elif first_char.lower() == "b":
                buySeating()
        elif first_char.lower() == "v":
            concert_seats = readJson("seating.json")
            if len(concert_seats) != 0:
                printSeating(concert_seats)
            else:
                concert_seats = createSeating()
                printSeating(concert_seats)
        elif first_char.lower() == "s":
            searchName()
        
        elif first_char.lower() == "d":
            readReciepts()
        
        else:
            print("ERROR: no such command")

# call main function to start program
main()