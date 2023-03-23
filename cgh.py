import openpyxl
import xlrd

ws = xlrd.open_workbook("Оборотная_ведомость_по_НФА_форма_0504035_108_51.xls")
# ws=wb_obj.active
sh = ws.sheet_by_index(0)
a=set()
b=[]
kasnaRows=[]
for i in range(sh.nrows):
    print(sh.row(i)[12].value)

print(len(a))
print(len(b))
# print(kasnaRows[4:])
print(len(kasnaRows))
print(len(kasnaRows[4:]))
kasnaRows=kasnaRows[4:0]
dup = [x for i, x in enumerate(b) if i != b.index(x)]
print(dup)
# Give the location of the file
# path = "_1 РАЗДЕЛ КАЗНА НА 31.12.2022 .xlsx"
#
#
# # To open the workbook
# # workbook object is created
# wb_obj = openpyxl.load_workbook(path)
# ws=wb_obj.active
# a=set()
# b=[]
# kasnaRows=[]
# for i in ws.values:
#     kasnaRows.append(i)
#     if i[58]!=None:
#         a.add(i[58].strip())
#         b.append(i[58].strip())
#     else:
#         print('blblblmmmm))))))))))))))')
#
# print(len(a))
# print(len(b))
# # print(kasnaRows[4:])
# print(len(kasnaRows))
# print(len(kasnaRows[4:]))
# kasnaRows=kasnaRows[4:0]
# dup = [x for i, x in enumerate(b) if i != b.index(x)]
# print(dup)
