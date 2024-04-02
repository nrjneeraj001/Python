# Question 1.
# *
# **
# ***
# ****
# *****
# for i in range (1,6):                
#     for j in range (1,i+1):          
#         print("*",end=" ")           
#     print("")                        



# Question 2.
# 1
# 22
# 333
# 4444
# for i in range (1,5):                  
#     for j in range (i):                
#         print(i,end="")                
#     print("")                          


# Question 3.
# 1
# 12
# 123
# 1234
# for i in range (1,5):                    
#     for j in range (1,i+1):              
#         print (j,end=" ")                
#     print (" ")                          


# Question 4.
# 4321
# 432
# 43
# 4
# for i in range (1,5):                     
#     for j in range (4,i-1,-1):            
#         print(j,end=" ")                  
#     print(" ")                            


# Question 5.
# 1
# 23
# 456
# 78910
# num = 1                                    
# for i in range (1,5):                      
#     for j in range (i):                    
#         print(num,end=" ")                 
#         num+=1                             
#     print(" ")                  


# Question 6.
# A
# AB
# ABC
# ABCD
# for i in range (1,5):                      
#     for j in range (i):                    
#         print(chr(65+j),end=" ")           
#     print (" ")                            


# Question 7.
# *****
# ****
# ***
# **
# *
# for i in range (5,0,-1):                   
#     for j in range (i):          
#         print("*",end=" ")           
#     print(" ")   


#Question 8.
# 12345
# 1234
# 123
# 12
# 1
# for i in range (5,0,-1):                     
#     for j in range (1, i+1):                 
#         print(j,end=" ")                     
#     print(" ")                               
#                                              


# Question 9.
# ABCD
# ABC
# AB
# A
# for i in range (4,0,-1):                     
#     for j in range (i):                     
#         print(chr(65+j),end=" ")            
#     print (" ")                             


# Question 10.
# FEDCBA
# FEDCB
# FEDC
# FED
# EF
# F
# for i in range (6,0,-1):
#     for j in range (i):
#         print(chr(70-j),end=" ")
#     print("")


for i  in range (1,6):
    for j in range(1,i):
        print(" ",end=" ")
    for k in range (5,i-1,-1):
        print("*",end=" ")
    print(" ")