import io
from django.http import HttpResponse
import matplotlib.pyplot as plt
import threading
import numpy as np
from django.db import connection
from itertools import accumulate
from .customers import hours
import psycopg2
import multiprocessing


def sells(request, width, height, dpi=72):
    # Извлекаем данные из базы данных

    #conn = psycopg2.connect("dbname=postgres user=postgres", password='1111')
    
    with connection.cursor() as cursor:
        cursor.execute('''
        select sell_date::time, alcohol, confections, others
            from sell_data.sells
            where sell_date::date = %s::date 
            order by sell_date ;
        ''', ('2018-10-01',))  # если переменная то подставлять нужно кортеж (требует джанго)

        dt = np.array([  ( hours(x), float(a), float(c), float(o) ) for (x,a,c,o) in cursor]) #данные в виде кортежа, преобразовываем в массив numpy

    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)
    tm = np.array(dt[:,0])
    al = np.array([ x for x in accumulate(dt[:,1]) ]) / 1e6
    cn = np.array([ x for x in accumulate(dt[:,2]) ]) / 1e6
    ot = np.array([ x for x in accumulate(dt[:,3]) ]) / 1e6

    # Тут формируем картинку (отрисовываем)
    ax.plot(tm, al)
    ax.plot(tm, cn)
    ax.plot(tm, ot)
    
    ax.set_xlim(0,24) #пределы изменения гистограммы
    ax.set_xticks(list(range(0,25,3))) #отметки через каждые 3 часа
    fig.tight_layout()
    

    buf = io.BytesIO()
    fig.savefig(buf, format='PNG')

    return HttpResponse( buf.getvalue(), content_type='image/png' )
