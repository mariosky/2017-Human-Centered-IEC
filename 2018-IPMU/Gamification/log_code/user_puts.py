
import sqlite3

conn = sqlite3.connect('log.db')
c = conn.cursor()

# logs table: timestamp, IP , level , user , worker
c.execute(
    """ SELECT user , count(*)
        FROM logs
        WHERE user <> 'anonimo'
        GROUP BY user
        ORDER BY 2 DESC
""")

users = [r[1]  for r in c]


c.execute(
        """ SELECT IP , count(*)
            FROM logs
            WHERE user == 'anonimo'
            GROUP BY IP
            ORDER BY 2 DESC
    """)

IPs = [r[1] for r in c]


# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, MaxNLocator

x_users = range(len(users))
x_ips = range(len(IPs))

print len(users)
# automatically update ylim of ax2 when ylim of ax1 changes.
fig , ax =plt.subplots()
ax.plot(x_users,users,'g^')
ax.plot(x_ips,IPs,'r.')
ax.set_yscale('log')
ax.axis([1, 100, 1, 100000])
for axis in [ax.xaxis, ax.yaxis]:
    axis.set_major_formatter(ScalarFormatter())

ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_ylabel('PUTs')
ax.set_xlabel('Users')
ax.grid(True)

plt.show()


#x_ips = range(len(IPs))
#print len(IPs)
#fig , ax =plt.subplots()
#print IPs
#ax.plot(x_ips,IPs,'.')
#ax.set_yscale('log')
#ax.axis([1, 100, 1, 100000])
#for axis in [ax.xaxis, ax.yaxis]:
#    axis.set_major_formatter(ScalarFormatter())

#ax.xaxis.set_major_locator(MaxNLocator(integer=True))
#ax.set_ylabel('PUTs')
#ax.set_xlabel('IPs')
#ax.grid(True)
#plt.show()

