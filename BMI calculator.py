# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Function to classify BMI
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Get user input
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight, height)

# Classify BMI
category = classify_bmi(bmi)

# Print the results
print(f"Your BMI is {bmi:.2f}")
print(f"You are classified as: {category}")
