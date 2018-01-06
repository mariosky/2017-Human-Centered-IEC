import  sqlite3
import time
conn = sqlite3.connect('log.db')
c = conn.cursor()

# logs table: timestamp, IP , level , user , worker
c.execute(
    """ SELECT datetime((strftime('%s', timestamp) / 15) * 15, 'unixepoch') interval, count(distinct worker)
        FROM logs
        WHERE user = 'd625621a78a8362a0b39d2306a433944c7b987df'
        GROUP BY interval
        ORDER BY interval
""")

users = [( time.mktime(time.strptime(r[0],'%Y-%m-%d %H:%M:%S' )),r[1], r[0]) for r in c]
conn.close()


ticks =[(1479994980.0, 0, u'05:43:00'),
    (1480043640.0, 2880, u'19:14:00'),
    (1480058790.0, 3840, u'23:26:30'),
    (1480074180.0, 4320, u'03:43:00'),
    (1480089930.0, 4800, u'08:05:30'),
    (1480104345.0, 5760, u'12:05:45'),
    (1480153065.0, 6720, u'01:37:45'),
    (1480260390.0, 7200, u'07:26:30'),
    (1480322565.0, 7680, u'00:42:45')]




import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, MaxNLocator


fig , ax =plt.subplots()

ax.plot( [ u[0] for u in users] , [ u[1] for u in users],'g.')

ax.set_ylabel('Workers')
ax.set_xlabel('15 second slots')
ax.grid(True)

plt.xticks([t[0] for t in ticks] , [t[2] for t in ticks] , rotation=30)
plt.show()