import  sqlite3
import time
conn = sqlite3.connect('log.db')
c = conn.cursor()

# logs table: timestamp, IP , level , user , worker
c.execute(
    """ SELECT datetime((strftime('%s', timestamp) / 900) * 900, 'unixepoch') interval, count(*)
        FROM logs
        WHERE user <> 'anonimo'
        GROUP BY interval
        ORDER BY interval
""")

users = [( time.mktime(time.strptime(r[0],'%Y-%m-%d %H:%M:%S' )),r[1]) for r in c]


c.execute(
    """ SELECT datetime((strftime('%s', timestamp) / 900) * 900, 'unixepoch') interval, count(*)
        FROM logs
        WHERE user = 'anonimo'
        GROUP BY interval
        ORDER BY interval
""")

IPs = [( time.mktime(time.strptime(r[0],'%Y-%m-%d %H:%M:%S' )),r[1]) for r in c]


conn.close()


import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, MaxNLocator


fig , ax =plt.subplots()

ax.plot( [ u[0] for u in users] , [ u[1] for u in users],'g.')
ax.plot( [ i[0] for i in IPs] , [ i[1] for i in IPs],'b^')
ax.set_ylabel('PUTs')
ax.set_xlabel('15 minute slots (unix epoch)')
ax.grid(True)

plt.show()