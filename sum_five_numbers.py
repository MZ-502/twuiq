# برنامج يجمع خمسة ارقام
numbers = []
for i in range(5):
    num = float(input("ادخل رقم: "))
    numbers.append(num)
total = sum(numbers)
print("مجموع الارقام =", total)
