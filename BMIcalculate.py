# To Calculate BMI class work
# 18/07/2025- friday  day4
height_m=float(input("Enter your height in Metre: "))
weight_kg=float(input("Enter your weight in Kilogram: "))
bmi=weight_kg/(height_m**2)
print("your BMI is: ",bmi)

if bmi<18.5:
    print("Under_Weight ")
elif 18.5 <= bmi < 24.9:
    print("Optimum_Weight ")
elif 25 <= bmi <29.9:
    print("Over_Weight ")
else:
    print("Obsesity")

    