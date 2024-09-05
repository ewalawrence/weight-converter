# Python Weight Converter

weight = float(input("Enter your weight: "))
unitOfConversion = input("kilograms or Pounds? (K or P): ").upper()

if unitOfConversion == "K":
    weight = round(weight * 2.205, 1)
    unit = "Lps"
    print(f"Your current weight is: {round(weight, 1)}{unit}")
elif unitOfConversion == "P":
    weight = round(weight / 2.205, 1)
    unit = "kg"
    print(f"Your current weight is: {round(weight, 1)}{unit}")

else:
    print(f"{unitOfConversion} is not valid unit of conversion")