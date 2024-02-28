import random                                                                                      
import sys                                              
import time                                             
brd1=[1,2,3]
brd2=[4,5,6]
brd3=[7,8,9]             
print(brd1)
print(brd2)
print(brd3)
#List of available and used positions                   
empty = [1,2,3,4,5,6,7,8,9]                                                                         
#Deciding who begins                                    
random_number = random.randint(1,2)                     
while empty:                                            
    if random_number == 1:                              
        comp_desn="X"                                   
        user_desn="O"                                   
        sys.stdout.write("Comp plays")
        for i in range(4):                              
            sys.stdout.write('.')                       
            time.sleep(0.50)                            
        print(" ")
        comp_choice = int(random.randint(1,9))               
        if comp_choice in empty:
            print("comp chooses:",comp_choice)
            empty.remove(comp_choice)                                
            if comp_choice>6 & comp_choice<=9:                          
                brd3[comp_choice-7] = "X"       
            elif comp_choice>3 & comp_choice<6:         
                brd2[comp_choice-4] = "X"       
            elif comp_choice<=3:        
                brd1[comp_choice-1] = "X"        
            print(brd1)
            print(brd2)
            print(brd3)
            sys.stdout.write("User plays")           
            for i in range(4):                              
                sys.stdout.write('.')                       
                time.sleep(0.50)                            
            print(" ") 
            user_choice=int(input("enter posn no: "))                  
            empty.remove(user_choice)                                 
            if user_choice>6 & user_choice<=9:                          
                brd3[user_choice-7] = "O"       
            elif user_choice>3 & user_choice<6:         
                brd2[user_choice-4] = "O"       
            elif user_choice<=3:        
                brd1[user_choice-1] = "O"       
        else:                                           
            comp_choice = int(random.randint(1,9))
        print(brd1)
        print(brd2)
        print(brd3)
    else:                                               
        user_desn="X"                                   
        comp_desn="O"                                   
        sys.stdout.write("User plays")           
        for i in range(4):                              
            sys.stdout.write('.')                       
            time.sleep(0.50)                            
        print(" ")                                      
        user_choice=int(input("enter posn no: "))       
        empty.remove(user_choice)                                        
        if user_choice>6 & user_choice<=9:                          
            brd3[user_choice-7] = "X"           
        elif user_choice>3 & user_choice<6:             
            brd2[user_choice-4] = "X"           
        elif user_choice<=3:        
            brd1[user_choice-1] = "X"           
        print(brd1)
        print(brd2)
        print(brd3)
        sys.stdout.write("Comp plays")           
        for i in range(4):                              
            sys.stdout.write('.')                       
            time.sleep(0.50)                            
        print(" ") 
        comp_choice = int(random.randint(1,9))
        if comp_choice in empty:
            print("comp chooses:",comp_choice)
            empty.remove(comp_choice)                                
            if comp_choice>6 & comp_choice<=9:                          
                brd3[comp_choice-7] = "O"       
            elif comp_choice>3 & comp_choice<6:         
                brd2[comp_choice-4] = "O"       
            elif comp_choice<=3:        
                brd1[comp_choice-1] = "O"        
        else:                                           
            comp_choice = int(random.randint(1,9))        
        print(brd1)
        print(brd2)
        print(brd3)
else:                                                   
    print("Game over!")
#if 
