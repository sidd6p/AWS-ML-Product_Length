import pandas as pd
import csv


df_s = pd.read_csv(
    "C:\\Users\\siddpc\\OneDrive\\Desktop\\Projects\\AWS-ML-Product_Length\\dataset\\train_small.csv",
    encoding="unicode_escape",
)
# # Generate some random data
cat = list()

for x in df_s["PRODUCT_LENGTH"]:
    if x > 100000:
        cat.append(10000)
    elif x > 10000:
        cat.append((x // 10000) * 1000)
    elif x > 2000:
        cat.append((x // 1000) * 100)
    elif x > 100:
        cat.append((x // 100) * 10)
    else:
        cat.append(x // 10)

with open(
    "C:\\Users\\siddpc\\OneDrive\\Desktop\\Projects\\AWS-ML-Product_Length\\dataset\\train_small_cat.csv",
    "w",
    newline="",
) as file:
    writer = csv.writer(file)
    for a, c in zip(df_s["PRODUCT_LENGTH"], cat):
        writer.writerow([a, c])
