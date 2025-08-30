def hitung_bmi(height, weight):
    if height <= 0:
        return "Tinggi tidak boleh nol atau negatif."
    
    bmi = weight / (height ** 2)
    return bmi

weight = input("Enter your weight in kg: ")
height = input("Enter your height in meters: ")

bmi_saya = hitung_bmi(float(height), float(weight))
print("Your BMI is:", bmi_saya)

if isinstance(bmi_saya, (float, int)):
    if bmi_saya < 18.5:
        print("Kategori: Kurus")
    elif 18.5 <= bmi_saya < 24.9:
        print("Kategori: Normal")
    elif 25 <= bmi_saya < 29.9:
        print("Kategori: Gemuk (Overweight)")
    else:
        print("Kategori: Obesitas")