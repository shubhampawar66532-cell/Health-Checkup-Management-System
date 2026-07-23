import pandas as pd

# Load CSV
df = pd.read_csv("health.csv")

# Calculate BMI
df["Height_m"] = df["Height_cm"] / 100
df["BMI"] = df["Weight_kg"] / (df["Height_m"] ** 2)

# BMI Category
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

df["BMI_Category"] = df["BMI"].apply(bmi_category)

# Display Results
print("\n===== HEALTH REPORT =====")
print(df[["Patient_ID", "Age", "Gender", "BMI", "BMI_Category"]])

print("\nAverage BMI:", round(df["BMI"].mean(), 2))
print("Highest BMI:", round(df["BMI"].max(), 2))
print("Lowest BMI:", round(df["BMI"].min(), 2))