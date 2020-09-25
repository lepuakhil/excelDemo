from django.shortcuts import render

import xlwt
from django.http import HttpResponse
from .models import Student


def index(request):
    return render(request, 'home.html')


def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="student.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Student Data')  # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Name', 'School name', 'Standard' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Student.objects.all().values_list('name', 'school', 'grade')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response
