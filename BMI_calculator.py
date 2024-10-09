weight = float(input("Enter your wait in kg:"))
height = float(input("Enter your height in meter:"))
BMI = weight / height**2
print("Your BMI is :" , BMI)
if  BMI < 18.5 :
 print("You are Underweight")
elif 18.5 <= BMI < 24.9 :
 print("You are normal")

elif 25 <= BMI :
 print("You are overweight")