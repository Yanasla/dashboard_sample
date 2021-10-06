import io
from django.http import HttpResponse
import matplotlib.pyplot as plt
import threading
import numpy as np
from django.db import connection
import psycopg2


def day_res(request, width, height, dpi=72):
    # Извлекаем данные из базы данных

    #conn = psycopg2.connect("dbname=postgres user=postgres", password='1111')
    
    with connection.cursor() as cursor:
        cursor.execute('''
        select sum(alcohol), sum(confections), sum(others)
            from sell_data.sells
            where sell_date::date = %s::date ;
        ''', ('2018-10-01',))  # если переменная то подставлять нужно кортеж (требует джанго)

        a, c, o = cursor.fetchone()
        dt = np.array([ float(a), float(c), float(o) ]) #данные в виде кортежа, преобразовываем в массив numpy

    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)

    # Тут формируем картинку (отрисовываем)

    labels = ['АЛКОГОЛЬ', 'КОНДИТЕРКА', 'ПРОЧЕЕ']
    expl = [0.05, 0.05, 0.05]

    ax.pie( dt, labels=labels, explode=expl, shadow=True, autopct='%1.1f%%')
    ax.axis('equal')

    fig.tight_layout()

    buf = io.BytesIO()
    fig.savefig(buf, format='PNG')

    return HttpResponse( buf.getvalue(), content_type='image/png' )
