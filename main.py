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

