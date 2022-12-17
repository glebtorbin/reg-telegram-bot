import xlsxwriter

from get_last_5 import get_last_5


def create_file():
    workbook = xlsxwriter.Workbook('app/hi.xlsx')
    worksheet = workbook.add_worksheet('first_sheet')
    worksheet.write(0, 0, 'ФИО')
    worksheet.write(0, 1, 'Дата Рождения')
    worksheet.write(0, 2, 'Наименование роли')
    col = 0
    for pos in get_last_5():
        worksheet.write(col+1, 0, pos[0])
        worksheet.write(col+1, 1, pos[1])
        worksheet.write(col+1, 2, pos[2])
        col = col + 1
    workbook.close()



