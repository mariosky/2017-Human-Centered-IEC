import  sqlite3
import time
conn = sqlite3.connect('log.db')
c = conn.cursor()

# logs table: timestamp, IP , level , user , worker
c.execute(
    """ SELECT user, count(distinct IP), count(distinct worker), count(*)
        FROM logs
        WHERE user <> 'anonimo'
        GROUP BY user
        ORDER BY 2 desc, user
""")

users = [ r for r in c]
conn.close()
print users[0]

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def log_10_product(x, pos):
    """The two args are the value and tick position.
    Label ticks with the product of the exponentiation"""
    return '%1i' % (x)

colors = np.random.rand(len(users))

fig , ax = plt.subplots()

ax.set_yscale('log')
ax.set_xscale('log')
ax.set_ylabel('PUTs')
ax.set_xlabel('Workers')
ax.set_ylim(1e-1, 1e7)
ax.set_xlim(1e-1, 1e5)
formatter = FuncFormatter(log_10_product)
ax.xaxis.set_major_formatter(formatter)
ax.yaxis.set_major_formatter(formatter)

ax.grid(True)




ax.scatter([ u[2] for u in users], [ u[3] for u in users], s=[ u[1]*50 for u in users], c=colors, alpha=0.5)

plt.show()




