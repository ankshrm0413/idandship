#id and ship
t=int(input())
while(t!=0):
    n=input()
    if(n=='B' or n=='b'):
        print('BattleShip')
    
    elif(n=='C' or n=='c'):
        print('Cruiser')
        
    elif(n=='D' or n=='d'):
        print('Destroyer')
        
    elif(n=='F' or n=='f'):
        print('Frigate')
        
    t-=1