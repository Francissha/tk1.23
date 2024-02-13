import random, sys

numbers={1: "one",2:"two", 3:"three", 4:"four", 5:"five", 6:"six"}

wallet=5000
while True: #main loop
    print("You have ", wallet, "how much do you bet (or QUIT) ? ")
    while True:
        pot=input("> ")
        
if pot.upper()==("QUIT"):  
     print("Thanks for playing")
     sys.exit()
     
elif not pot.isdecimal():
     print("Please enter a number")
     
elif int (pot) > wallet:
    print("You do not have enough to make that bet") 
    
else:
    pot=int(pot)         
    break #exit loop once bet is placed  
       
dice1=random.radint(1, 6)
dice2=random.radint(1, 6)      
print('The dealer swirls the cup and you hear the rattle of dice.')
print('The dealer slams the cup on the floor, still covering the')
print('dice and asks for your bet.')
print()
print(' CHO (even) or HAN (odd)?') 

while True:
    bet = input('> ').upper()
if bet != 'CHO' and bet != 'HAN':
    print('Please enter either "CHO" or "HAN".')
    continue
else:
    break





