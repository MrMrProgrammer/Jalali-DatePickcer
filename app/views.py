from itertools import groupby

from django.shortcuts import render

from jdatetime import datetime, date


def jalali_to_gregorian(jalali_date):
    jalali_datetime = datetime.strptime(jalali_date, "%Y/%m/%d").date()
    gregorian_datetime = jalali_datetime.togregorian()
    return gregorian_datetime


def index(request):
    if request.method == 'POST':
        print("it is post")

        date_value = request.POST.get('date')

        gregorian_date = jalali_to_gregorian(date_value)

        print(gregorian_date)


        return render(request, 'index.html')

    return render(request, 'index.html')
