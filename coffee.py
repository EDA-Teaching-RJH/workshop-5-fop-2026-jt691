due = 75
accepted_coins = [50, 20, 10 ,5 ]    #states the coin value that the machine will accept

while due > 0:   
        coin = int(input("insert coins"))   


        if coin in accepted_coins:
            due -= coin                  # coin value must be within accepted_value , due -= coin is the same as due = due - coin(this is done to keep the value )
            print ("Amount due:" , due )
    
        else:
            print("Invalid coin entered, please enter", abs(due))       # abs makes the value positive
    
# else:


print("Change owed:", abs(due))


  
    
    
    
    

