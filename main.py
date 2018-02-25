import xlwt as xl
book=xl.Workbook()
sheet=book.add_sheet("timestable")
for rows in range(1,1300):
    for cols in range(1,130):
        string1=cols
        sheet.write(rows-1,cols-1,rows+cols)

book.save("F:/excel_output/mathtable.xls")
