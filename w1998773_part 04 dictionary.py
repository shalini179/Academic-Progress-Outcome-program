# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID:20221710  UOW ID:w1998773
# Date:
#task04 dictionary 
#URL: https://stackoverflow.com/questions/3545331/how-can-i-get-dictionary-key-as-variable-directly-in-python-not-by-searching-fr.

choice = 'y' #identifying variables 
pass_c = 0
defer_c = 0
fail_c = 0
progress = 0
trailer = 0
retriever = 0
excluded = 0
total_c = 0
dict_list = []
final = []

while choice == 'y':  #checking data 
    dict = {'ID':0 , 'Outcome':0 , 'marks':0} #creating a dictionary 
    student_ID = str(input("Enter your UOW number : "))
    dict['ID'] = student_ID
    
    while True:
        pass_c = input(" please enter your credits at pass: ")
        if pass_c.isdigit (): #checking whether its integer or not 
                pass_c =int(pass_c)
                if pass_c not in range (0,121,20):
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
                if defer_c not in range (0,121,20): #checking ranage 
                     print("out of range ")
                else:
                    defer_c = int(defer_c)
                    break
        else:
            print("integer required.")
            
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

    total_c = pass_c + defer_c + fail_c

    if total_c > 120:
        print("total incorrect")
    else:
        
        if pass_c == 120:   #cheking credits 
            print("Progress")
            marks = [pass_c,defer_c,fail_c]
            dict['marks'] = marks
            dict['Outcome'] = 'Progress'
        elif pass_c >= 100 and pass_c <= 120:
            print("Progress (module trailer)")
            marks = [pass_c,defer_c,fail_c]
            dict['marks'] = marks
            dict['Outcome'] = 'Progress (module trailer)'
        elif fail_c >= 80:
            print("Exclude")
            marks = [pass_c,defer_c,fail_c]
            dict['marks'] = marks
            dict['Outcome'] = 'Exclude'
        else:
            0<=pass_c<=80
            print("Do not progress - module retriever")
            marks = [pass_c,defer_c,fail_c]
            dict['marks'] = marks
            dict['Outcome'] = 'Do not progress - module retriever'
    

    dict_li = [dict['ID'],dict['Outcome'],dict['marks']]
    dict_variable = (f"{dict['ID']}:{dict['Outcome']}-{dict['marks']}")
    dict_list.append(dict_variable)
    
    print()
    print("Would you like to enter set of data?")
    choice = input("Enter 'y' for yes or 'q' to quit and view results: ").lower()
    print()
    
print(' '.join(dict_list))      
        

