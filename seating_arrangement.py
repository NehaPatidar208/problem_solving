"""Akash and Vishal are quite fond of travelling.
They mostly travel by railways.
They were travelling in a train one day and
they got interested in the seating arrangement of their compartment.

HINT: II class sitting having 108 seats
 print the facing seat-number and the seat-type,
 separated by a single space in a new line.

Window Seat : WS
Middle Seat : MS
Aisle Seat : AS

"""
n=int(input("Enter the of sets whoes facing seat be know"))       
for i in range (0,n):
    t=int(input())
    s=t%12
    if(s <=6 and s!=0):
        g=t+(6-(s%7))*2+1
    elif(s==0):
        g=t-11
    else:
        g=t-((s%6)*2)+1
    
    if ((g%6==0) or (g%6==1)):
        print(g,"WS")
    elif((g%6==2) or (g%6==5)):
        print(g,"MS")
    else:
        print(g,"AS")
