import math

def calculate_bsa(height, weight, age, is_male):
    """
    Calculate Body Surface Area (BSA) using the Du Bois formula.
    
    Parameters:
        - height: Height of the person in centimeters.
        - weight: Weight of the person in kilograms.
        - age: Age of the person in years.
        - is_male: Boolean value indicating whether the person is male or female.
        
    Returns:
        The calculated BSA in square meters.
    """
    if is_male:
        bsa = 0.20247 * math.pow(height, 0.725) * math.pow(weight, 0.425) * math.pow(age, -0.202)
    else:
        bsa = 0.20247 * math.pow(height, 0.725) * math.pow(weight, 0.425) * math.pow(age, -0.156)
    
    return bsa

# Example usage
height = 175 # cm
weight = 70 # kg
age = 30 # years
is_male = True

bsa = calculate_bsa(height, weight, age, is_male)
print("Body Surface Area:", bsa, "m^2")
