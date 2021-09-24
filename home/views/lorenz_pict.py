import io
from django.http import HttpResponse
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D


def _lorenz(a, b, c, s=10, r=28, m=2.667):
    a_dot = s*(b-a)
    b_dot = r*a - b - a*c
    c_dot = a*b - m*c
    return a_dot, b_dot, c_dot


def lorenz_pict(request, width, height, dpi=72):

    dt = 0.01
    step_cnt = 10000

    ak = np.empty((step_cnt +1, ))
    bk = np.empty((step_cnt + 1,))
    ck = np.empty((step_cnt + 1,))

    ak[0] = 0.00
    bk[0] = 1.00
    ck[0] = 1.05

    for i in range(0, step_cnt):
        a_dot, b_dot, c_dot = _lorenz(ak[i], bk[i], ck[i])
        ak[i + 1] = ak[i] + (a_dot*dt)
        bk[i + 1] = bk[i] + (b_dot*dt)
        ck[i + 1] = ck[i] + (c_dot*dt)

    fig = plt.figure( figsize=(width/dpi, height/dpi), dpi=dpi)

    ax = fig.gca( projection='3d')

    ax.plot(ak, bk, ck, lw=0.5)

    buf = io.BytesIO()
    fig.savefig(buf, format='PNG')

    return HttpResponse( buf.getvalue(), content_type='image/png')
