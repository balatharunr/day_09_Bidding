dic = {}
def bid_win(d):
    max_val = max(d.values())
    winner = ""
    for key in d:
        if d[key] == max_val:
            winner = key
    print(winner," is the winner, bidding $",max_val)
while True:
    name = input("Enter the Name: ")
    bid = float(input("Enter Bid amount $"))
    dic[name] = bid
    choice = input("Do you need to continue(Y/N): ").lower()
    if choice == "n":
        bid_win(dic)
        print(''' 
            $$ $             
             \O/$            
            $ |              
             /_\             
           _|___|_           
         _|___|___|_         
       _|___|___|___|_       
     _|___|___|___|___|_     
   _|___|___|___|___|___|_   
 _|___|___|___|___|___|___|_ 
|___|___|___|___|___|___|___|
 \o/ \o/ \o/ \o/ \o/ \o/ \o/ 
  |   |   |   |   |   |   |  
 / \ / \ / \ / \ / \ / \ / \ ''')
        break
