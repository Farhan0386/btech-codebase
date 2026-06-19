total1 = 0
total2 = 0
count = 0

data = [
    [10, 20],
    [15, 25],
    [30, 40],
    [50, 60],
    [20, 30]
]

for row in data:
    try:
        total1+=float(row[0])
        total2+=float(row[1])
        count+=1
    except:
        print("Invalid row")
if count > 0:
    print("Column 1 Average =", total1/count)
    print("Column 2 Average =", total2/count)
else:
    print("No valid data found")