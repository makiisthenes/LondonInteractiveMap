import os

boroughs = []
b_path = os.path.join(os.getcwd(),"LondonBoroughs.txt")
with open(b_path, "r") as f:
    for line in f:
     line = line.strip()
     if len(line) is not None:
      print(line)
      boroughs.append(line)


for i in boroughs:
 j_path = os.path.join(os.getcwd(), f"BoroughJSON\\{i}")
 os.mkdir(j_path)
print("done")