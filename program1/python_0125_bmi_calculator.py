# Requirement: get input from the user about his height in meters and weight in kg.
# Calculate his bmi based on this formula:
# bmi = weight / (height ** 2)
# Print information based user's bmi value
# bmi in [0, 16)    : You are severely underweight
# bmi in [16, 18.5) : You are underweight
# bmi in [18.5, 25) : You are healthy
# bmi in [25, 30)   : You are overweight
# bmi in [30, max)  : You are severely overweight




# PART 1) DEFINE VARIABLES ====================================

# type 1) DEFEIN VARIABLES FROM THE QUESTION ------------------
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))

# Type 2) DEFINE VARIABLE WHICH IS TO SAVE THE RESULT ---------
bmi = 0
msg = ''

# Type 3) OTHER EXTRA VARIABLES ------------------------------


# PART 2) YOUR ALGO ===========================================

bmi = weight / (height ** 2)

if 0 <= bmi < 16:
    msg = 'You are severely underweight'

elif 16 <= bmi < 18.5:
    msg = 'You are underweight'

elif 18.5 <= bmi < 25:
    msg = 'You are healthy'

elif 25 <= bmi < 30:
    msg = 'You are overweight'

else:
    msg = 'You are severely overweight'


# PART 3 PRINT THE RESULT =====================================
print(f"Your BMI is: {bmi:.3f}")
print(msg)
