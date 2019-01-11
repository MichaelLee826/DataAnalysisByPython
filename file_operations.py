import os
import xlsxwriter

# 创建文件夹
fileName = 'MyExcelFile'
if fileName not in os.listdir():
    os.mkdir(fileName)

# 进入文件夹
os.chdir(fileName)

# 创建Excel文件
workbook = xlsxwriter.Workbook('Hello_World.xlsx')

# 新增一个名为'表1'的表单
worksheet = workbook.add_worksheet('表1')

# 在A1单元格中写入数据
worksheet.write('A1', "Hello Michael!")

# 关闭Excel文件
workbook.close()
