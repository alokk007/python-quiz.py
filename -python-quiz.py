print("WELCOME TO PYTHON QUIZ!!!")
playing=input("DO YOU WANT TO PLAY??")
if playing.lower()!="yes":
    quit()
print("OKAY!!LETS PLAY!!")
score=0
answer=input("who developed python?")
if answer.lower()=="guido van rossum":
    print("correct answer!")
    score=score+1
else:
    print("incorect answer")   
answer=input("what can python do?")
if answer.lower()=="server to create web application":
    print("correct answer!")
    score=score+1
else:
    print("incorect answer")   
answer=input("what is comments in python?")
if answer.lower()=="explain python code":
    print("correct answer!")
    score=score+1
else:
    print("incorect answer")  
answer=input("what is variable in python")
if answer.lower()=="container for storing data value":
    print("correct answer!")
    score=score+1
else:
    print("incorect answer")  
answer=input("what are work of operator?")
if answer.lower()=="operetions on variable and value":
    print("correct answer!")
    score=score+1
else:
    print("incorect answer")   
answer=input("what is datatypes?")
if answer.lower()=="variable can store data of different types":
    print("correct answer!")
    score=score+1
else:
    print("incorect answer")   
answer=input("which function used for known lenght of string?")
if answer.lower()=="len() function":
    print("correct answer!")
    score=score+1
else:
    print("incorect answer")   
answer=input("which types of method uesd for upper case?")
if answer.lower()=="upper() method":
    print("correct answer!")
    score=score+1
else:
    print("incorect answer")   
answer=input("which types of method uesd for lower case?")
if answer.lower()=="lower() method":
    print("correct answer!")
    score=score+1
else:
    print("incorect answer")
answer=input("what is string concatenation?")
if answer.lower()=="add two strings":
    print("correct answer!")
    score=score+1
else:
    print("incorect answer") 

print("you got"+str(score)+"question correct")
print("you have got :"+str((score/10)*100)+"%")
      
