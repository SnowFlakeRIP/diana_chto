import openpyxl

# Give the location of the file
path = "Оборотная_ведомость_по_НФА_форма_0504035_108_51.xls"

# To open the workbook
# workbook object is created
wb_obj = openpyxl.load_workbook(path)
ws = wb_obj.active
a = set()
b = []
kasnaRows = []
for i in ws.values:
    kasnaRows.append(i)
    # a=(set([i]))
    # print(len(a))
    if i[58] != None:
        a.add(i[13].strip())
        b.append(i[13].strip())
    else:
        print('blblblmmmm))))))))))))))')
    # for x in a:
    #     if x=

print(len(a))
print(len(b))
print(kasnaRows[4:])
print(len(kasnaRows))
print(len(kasnaRows[4:]))
kasnaRows = kasnaRows[4:0]
dup = [x for i, x in enumerate(b) if i != b.index(x)]
print(dup)  # [1, 5, 1]

# print(i[58])