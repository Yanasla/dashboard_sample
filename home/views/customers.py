import io
from django.http import HttpResponse
import matplotlib.pyplot as plt
import numpy as np
from django.db import connection


def hours(tm):
    #преобразует время суток в часы и доли часа
    x = tm.microsecond / 1000000.0
    x = (tm.second + x) / 60.0
    x = (tm.minute + x) / 60.0
    return tm.hour + x


def customers(request, width, height, dpi=72):
    #Извлекаем данные из базы данных

    with connection.cursor() as cursor:
        cursor.execute('''
        select sell_date::time
            from sell_data.sells
            where sell_date::date = %s::date ;
        ''', ('2018-10-01', ) )                 #если переменная то подставлять нужно кортеж (требует джанго)

        dt = np.array([ hours(x) for (x,) in cursor ])

    fig, ax = plt.subplots( figsize=(width/dpi,height/dpi), dpi=dpi )

    #Тут формируем картинку
    ax.hist(dt, bin=24*4)

    buf = io.BytesIO()
    fig.savefig(buf, format='PNG')

    return HttpResponse( buf.getvalue(), content_type='image/png' )
