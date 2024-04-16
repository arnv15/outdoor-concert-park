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

