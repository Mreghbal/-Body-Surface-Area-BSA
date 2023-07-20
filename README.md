# Body Surface Area (BSA) Calculation

## Table of Contents
- [Introduction](#introduction)
- [Usage](#usage)
- [How to Run](#how-to-run)
- [Explanation](#explanation)
- [Example Usage](#example-usage)
- [Follow Me](#follow-me)

## Introduction
This repository contains a Python code for calculating the Body Surface Area (BSA) using the Du Bois formula. BSA is an important measurement in medical calculations and is used in various clinical contexts, such as determining drug dosages, assessing nutritional needs, and evaluating cardiac output.

The Bois formula is one of several formulas commonly used to estimate BSA. It takes into account the person's height, weight, age, and gender to calculate the BSA in square meters. The formula differs slightly for males and females due to physiological differences.

## Usage
To use the code, you need to provide the following parameters:
- `height`: Height of the person in centimeters.
- `weight`: Weight of the person in kilograms.
- `age`: Age of the person in years.
- `is_male`: Boolean value indicating whether the person is male or female.

The code will then calculate the BSA using the Du Bois formula and return the result in square meters.

## How to Run
To run the code, follow these steps:

1. Make sure you have Python installed on your system.
2. Download or clone this repository to your local machine.
3. Open a terminal or command prompt and navigate to the directory where the code is located.
4. Run the following command to execute the code:

   ```
   python bsa_calculation.py
   ```

5. Follow the prompts enter the required parameters (height, weight, age, and gender).
6. The code will calculate the BSA and display the result.

## Explanation
The code uses the Du Bois formula to calculate the BSA. The formula is different for males and females due physiological differences. Here's an explanation of the formula:

For males:
``bsa = 0.20247 * height^0.725 * weight^0.425 * age^-0.202
```

For females:
```
bsa = 0.20247 * height^0.725 * weight^0.425 * age^-0.156
```

In these formulas, `height` is raised to the power of 0.725, `weight` is raised to the power of 0.425, and `age` is raised to the power of -0.202 for males or -0.156 for females. These values are then multiplied by appropriate coefficients and constants to calculate the BSA.

 calculated BSA represents the estimated total surface area of a person's body in square meters. is commonly used in medical calculations to adjust drug dosages, assess metabolic needs, and evaluate physiological parameters.

## Example Usage
Here's an example usage of the code:

```python
height = 175  # cm
weight = 70  #
age = 30  # years
is_male = True

bsa = calculate_bsa(height, weight, age, is_male)
print("Body Surface Area:", bsa, "m^2")
```

In this example, calculate the BSA for a male individual with a height of 175 cm, weight of 70 kg, and age of 30 years. The calculated BSA is then printed to the console.

## Follow Me
If you find this code useful, feel free to follow on LinkedIn and Twitter for more updates and resources:

LinkedIn: [Reza Eghbal](https://www.linkedin.com/in/mreghbal)

Twitter: [Reza Eghbal](https://twitter.com/mreghbal)

Thank you for your support!
