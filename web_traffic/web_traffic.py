import scipy as sp
import matplotlib.pyplot as plt


def error(f, x, y):
    return sp.sum((f(x) - y) ** 2)


data = sp.genfromtxt('web_traffic.tsv', delimiter='\t')
x = data[:,0]
y = data[:,1]
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

fpl, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)
f1 = sp.poly1d(fpl) # linear func
f2p = sp.polyfit(x, y, 2)
f2 = sp.poly1d(f2p)
f3p = sp.polyfit(x, y, 3)
f3 = sp.poly1d(f3p)
f10p = sp.polyfit(x, y, 10)
f10 = sp.poly1d(f10p)
f100p = sp.polyfit(x, y, 100)
f100 = sp.poly1d(f100p)

inflection = 3.5 * 7 * 24
xa = x[:inflection]
ya = y[:inflection]
xb = x[inflection:]
yb = y[inflection:]
fa = sp.poly1d(sp.polyfit(xa, ya, 1))
fpl2 = sp.polyfit(xb, yb, 1)
print fpl2
fb = sp.poly1d(fpl2)


plt.scatter(x, y)
plt.title('Web traffic over the last month')
plt.xlabel('Time')
plt.ylabel('Hits/Hour')
plt.xticks([w * 7 * 24 for w in range(10)], ['week %i'%w for w in range(10)])
plt.autoscale(tight=True)
fx = sp.linspace(0, x[-1], 1000)
plt.plot(fx, f1(fx), linewidth=4)
plt.plot(fx, f2(fx), linewidth=4)
plt.plot(fx, f3(fx), linewidth=4)
plt.plot(fx, f10(fx), linewidth=4)
plt.plot(fx, f100(fx), linewidth=4)
plt.plot(fx, fa(fx), linewidth=4)
plt.plot(fx, fb(fx), linewidth=4)
plt.legend(['d=%i' % f1.order, 'd=%i' % f2.order, 'd=%i' % f3.order, 'd=%i' % f10.order, 'd=%i' % f100.order], loc='upper left')
plt.grid()
plt.show()


