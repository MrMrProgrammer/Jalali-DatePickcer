jalali date picker :
  https://github.com/majidh1/JalaliDatePicker

ChatGPT code :

```markdown
pip install jdatetime
```

```markdown
from jdatetime import datetime, date

def jalali_to_gregorian(jalali_date):
    # تبدیل تاریخ Jalali به میلادی
    jalali_datetime = datetime.strptime(jalali_date, "%Y-%m-%d").date()
    gregorian_datetime = jalali_datetime.togregorian()
    return gregorian_datetime

from django.shortcuts import render
from .models import YourModel
from .forms import YourForm

def your_view(request):
    if request.method == 'POST':
        # فرم را از درخواست بگیرید
        form = YourForm(request.POST)

        if form.is_valid():
            # تبدیل تاریخ Jalali به میلادی
            jalali_date = form.cleaned_data['jalali_date']
            gregorian_date = jalali_to_gregorian(jalali_date)

            # ذخیره تاریخ میلادی در دیتابیس
            your_model_instance = form.save(commit=False)
            your_model_instance.gregorian_date = gregorian_date
            your_model_instance.save()

    else:
        form = YourForm()

    return render(request, 'your_template.html', {'form': form})
```
