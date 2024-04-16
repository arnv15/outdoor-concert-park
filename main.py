import numpy as np
import random
import json
import jsonpickle
import re
import uuid
import pandas as pd
pd.options.mode.chained_assignment=None
pd.set_option("max_colwidth", None)
pd.set_option('display.max_columns', None)

def createSeating():
    '''
        Reset all seatings and purge all purchases
    '''
    n_row = 20
    n_col = [chr(i) for i in range(ord('A'), ord('Z')+1)]
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
            seating.append({"col":c, "row":r, "Name":"", "Email":"", "Seat Type":seat_type, "Price":price,"Available":"."})        
    saveJson(seating, "seating.json")
   
    #purge receipt.json
    receipt=[]
    saveJson(receipt,"receipt.json")
   
    return seating

def readJson(filename):
    '''
        Read json file, then return an object
    '''
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
    '''
        Receive an object and write to filename with json format
    '''
           
    with open(filename , "w") as write:
        json.dump(seating, write, indent=2)
   
    try:
        seating_file = open(filename, "r")
    except IOError:
        print("Error: File " + filename + " does not appear to exist.")
        return -1      
   
def printSeating(seating):
    '''
        Print out seatings row, column, type, price, available or not
    '''
    n_row = 20
    n_col = 26
   
    #create array ["A", ..., "Z"] for seatings column
    alpha = [chr(i) for i in range(ord('A'), ord('Z')+1)]
   
    # range of seats
    frontSeat=range(5)
    middleSeat=range(5,11)
    backSeat=range(11,20)  
   
    # print seats
    print('-'*77)
    print(' '*35+'Seating')
    print('-'*77)

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
    print("[r] Reset seatings and purge all purchases")
    print("[q] quit")
    print("-"*77)

def main():
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
        if first_char.lower() == 'q':
            print("Thank you for using Outdoor Park Concert App!")
            user_quit = True
        # elif first_char.lower() == 'b':
        #     try:
        #         js_seating = pd.read_json('seating.json')
        #     except:
        #         print("Error: in load seatings. Please try again")
        #         concert_seats = createSeating()
               
        #     else:
        #         buySeating(js_seating)
        elif first_char.lower() == 'v':
            concert_seats=readJson("seating.json")
            if len(concert_seats)!=0:
                printSeating(concert_seats)
            else:
                concert_seats = createSeating()
                printSeating(concert_seats)
        # elif first_char.lower() == 's':
        #     searchName()
        
        # elif first_char.lower() == 'd':
        #     printPurchases()
        elif first_char.lower() == 'r':
            print("Reset all seatings and purge all history purchases")
            concert_seats = createSeating()
            printSeating(concert_seats)
        else:
            print("ERROR: no such command")

main()
