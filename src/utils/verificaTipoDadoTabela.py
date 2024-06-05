import chardet

with open("../dados/datatran2023_1trimestre.csv", "rb") as f:
    result = chardet.detect(f.read())
    print(result)
