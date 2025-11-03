with open("file1.txt") as f1:
    list_f1 = [int(x.strip()) for x in f1.readlines()]

with open("file2.txt") as f2:
    list_f2 = [int(x.strip()) for x in f2.readlines()]

result = [nums for nums in list_f1 if nums in list_f2]
print(result)