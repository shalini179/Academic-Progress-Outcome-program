# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID:20221710  UOW ID:w1998773
# Date:
#task01
#student version with histogram
choice='y'   #identifying variables
count=0
pass_c=0
defer_c=0
fail_c=0
progress=0
trailer=0
retriever=0
excluded=0
total=0

while choice == 'y':   #checking data 
    while True:     #asking for credits 
        pass_c = input(" please enter your credits at pass: ")
        if pass_c.isdigit (): #checking whether it is integer or not 
                pass_c =int(pass_c)
                if pass_c not in range (0,121,20):   #checking range of credits 
                     print("out of range ")
                else:
                    pass_c = int(pass_c)
                    break
        else:
            print("integer required.")
            
    while True:
        defer_c = input(" please enter your credits at defer: ")
        if defer_c.isdigit ():
                defer_c =int(defer_c)
                if defer_c not in range (0,121,20):
                     print("out of range ")
                else:
                    defer_c = int(defer_c)
                    break
        else:
            print("integer reqiuired.") #cheking data type
            
    while True:
        fail_c = input(" please enter your credits at fail: ")
        if fail_c.isdigit ():
                fail_c =int(fail_c)
                if fail_c not in range (0,121,20):
                     print("out of range ")
                else:
                    fail_c = int(fail_c)
                    break
        else:
            print("integer required.")
            
    total= int(pass_c) + int(defer_c) + int(defer_c)

    
    if (pass_c+defer_c+ fail_c) == 120:  #calculating total of credits       
            if pass_c==120:
                print ("Progress")
                progress += 1
            elif pass_c==100:
                print ("Progress (module trailer)")
                trailer += 1
            elif fail_c>=80:
                print ("Exclude ")
                excluded += 1
            elif pass_c <100:
                print ("Module retriever ")
                retriever += 1
    else :
        print ("Total incorrect ")
              


    print()
    print("would you like to enter another set of data ?: ")
    choice = input(" enter 'y' for yes and 'q' to quit and view results:")
    print()
    
print("-"*80)
print("Histogram")
print("Progress ",progress,"  : ",progress*"*")
print("Trailer ",trailer,"   : ",trailer* "*" )
print("Retriever", retriever,"  : ",retriever*"*")
print("Excluded", excluded,"   : ",excluded*"*")
print()

total = progress + trailer + retriever + excluded
print(total,"Outcomes in total.")
print("-"*80)


                

