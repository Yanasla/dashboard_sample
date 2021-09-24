#!/usr/bin/venv/python3
# -*- coding: utf-8 -*-

import io
from django.http import HttpResponse
import matplotlib.pyplot as plt
import numpy as np


def simple_picture(request, width, height, dpi=72):
    # Формирование картинки

    x = np.linspace(-100,100,10000)
    y = np.sin(x) / x

    fig, ax = plt.subplots(figsize=(width/dpi, height/dpi), dpi=dpi)
    ax.plot(x,y)

    buf = io.BytesIO()
    fig.savefig(buf, format='PNG')

    # Cохранить картинку в буфер
    return HttpResponse( buf.getvalue(), content_type='image/png' )
