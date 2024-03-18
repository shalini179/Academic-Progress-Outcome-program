# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID:20221710  UOW ID:w1998773
# Date:
#task02
pass_c = 0 #identifying varibles 
defer_c = 0
fail_c= 0
total = 0
progress = 0
trailer = 0
retriever = 0
excluded = 0
total = 0
choice = 'y'
progress_list = []
module_trailer_list = []
module_retriever_list = []
excluded_list = []

while choice =='y': #checking data 
    while True:
        pass_c = input("Please enter your credits at pass: ") #asking for credits 
        if pass_c.isdigit(): #checking whether its integer or not 
                pass_c = int(pass_c)
                if pass_c not in range(0,121,20):#cheking ranage of credits 
                    print("Out of range")
                else:
                    pass_c = int(pass_c)
                    break
        else:
            print("Integer required")
    while True:
        defer_c = input("Please enter your credits at defer: ")
        if defer_c.isdigit():
                defer_c= int(defer_c)
                if defer_c not in range(0,121,20):
                    print("Out of range")
                else:
                    defer_c = int(defer_c)
                    break
        else:
            print("Integer required")
    while True:
        fail_c = input("Please enter your credits at fail: ")
        if fail_c.isdigit():
                fail_c = int(fail_c)
                if fail_c not in range (0,121,20):
                    print("Out of range")
                else:
                    fail_c = int(fail_c)
                    break
        else:
            print("Integer required")

    total = int(pass_c) + int(defer_c) + int(fail_c)

    if total != 120:
        print("Total incorrect")
    else:
        if pass_c == 120: #adding credits to the list 
            print("Progress")
            progress = progress + 1
            progress_list.append(pass_c)
            progress_list.append(defer_c)
            progress_list.append(fail_c)
        elif pass_c == 100:
            print("Progress (module trailer)")
            trailer = trailer + 1
            module_trailer_list.append(pass_c)
            module_trailer_list.append(defer_c)
            module_trailer_list.append(fail_c)
        elif fail_c >= 80:
            print("Exclude")
            excluded = excluded + 1
            excluded_list.append(pass_c)
            excluded_list.append(defer_c)
            excluded_list.append(fail_c)
        else:
            0 <= pass_c <= 80
            print("Do not progress - module retriever")
            retriever = retriever + 1
            module_retriever_list.append(pass_c)
            module_retriever_list.append(defer_c)
            module_retriever_list.append(fail_c)


    print()
    print("Would you like to anter set of data?")
    choice = input("Enter 'y' fot yes or 'q' to quit and view results: ")
    print()

print("part 03")
progress_length = int(len(progress_list) / 3) #creating sub-lists to the display credits 
s = 0
for i in range(progress_length):
    print("Progress - ",progress_list[s],",",progress_list[s+1],",",progress_list[s+2])
    s = s + 3
trailer_length = int(len(module_trailer_list) / 3)
p = 0
for i in range(trailer_length):
    print("progress (module trailer) - ",module_trailer_list[p],",",module_trailer_list[p+1],",",module_trailer_list[p+2])
    p = p + 3
retriever_length = int(len(module_retriever_list) / 3)
r = 0
for i in range(retriever_length):
    print("module retriever - ",module_retriever_list[r],",",module_retriever_list[r+1],",",module_retriever_list[r+2])
    r = r + 3
excluded_length = int(len(excluded_list) / 3)
t = 0
for i in range(excluded_length):
    print("Excluded - ",excluded_list[t],",",excluded_list[t+1],",",excluded_list[t+2])
    t = t + 3

