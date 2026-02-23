A = 70 - 100
B = 60 - 69
C = 55 - 59 
D = 50 - 54 
E = 40 - 49
F = 0  - 39


name = input ("enter thy name:")
score = int(input("enter your score:"))

if score >= 70 and score <= 100:
    print(f"{name}  A has been given to thee")
elif score >= 60 and score < 70:
    print(f"{name} B has been given to thee")
elif score >= 55 and score <= 59:
    print(f"{name} C has been given to thee") 
elif score >= 50 and score <= 54:
    print(f"{name} D has been given to thee") 
elif score >= 40 and score <= 49:
    print(f"{name} E has been given to thee") 
elif score >= 0 and score <= 39:
    print(f"{name} F has been given to thee")    
else:
    print("depart from thy office u peasant")
