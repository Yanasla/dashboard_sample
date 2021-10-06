import io
from django.http import HttpResponse
import matplotlib.pyplot as plt
import numpy as np
from django.db import connection
from itertools import accumulate
import psycopg2
from .customers import hours


def hours(tm):
    # преобразует время суток в часы и доли часа
    x = tm.microsecond / 1000000.0
    x = (tm.second + x) / 60.0
    x = (tm.minute + x) / 60.0
    return tm.hour + x


def customers(request, width, height, dpi=72):
    # Извлекаем данные из базы данных

    conn = psycopg2.connect("dbname=postgres user=postgres")

    with conn.cursor() as curs:
        curs.execute('''
        select sell_date::time, alcohol, confections, others
            from sell_data.sells
            where sell_date::date = %s::date 
            order by sell_date ;
        ''', ('2018-10-01',))  # если переменная то подставлять нужно кортеж (требует джанго)

        dt = np.array([(hours(x), float(n), float(g), float(l)) for (x, n, g, l) in curs])

    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)

    tm = np.array(dt[:,0])
    al = np.array([ x for x in accumulate(dt[:,1]) ]) / 1e6
    cn = np.array([ x for x in accumulate(dt[:,2]) ]) / 1e6
    ot = np.array([ x for x in accumulate(dt[:,3]) ]) / 1e6

    ax.plot(tm, al)
    ax.plot(tm, cn)
    ax.plot(tm, ot)

    # Тут cформируем картинку
    ax.hist(dt, bins=24 * 4)

    ax.set_xlim(0, 24)  # пределы изменения гистограммы
    ax.set_xticks(list(range(0, 25, 3)))  # отметки через каждые 3 часа
    fig.tight_layout()

    buf = io.BytesIO()
    fig.savefig(buf, format='PNG')

    return HttpResponse(buf.getvalue(), content_type='image/png')
