
import  sqlite3

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

users = [r[1] for r in c]


c.execute(
        """ SELECT IP , count(*)
            FROM logs
            WHERE user == 'anonimo'
            GROUP BY IP
            ORDER BY 2 DESC
    """)

IPs = [r[1] for r in c]


# Save (commit) the changes
#conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

print len(IPs)
print len(users)

import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, MaxNLocator



x_users = range(len(users))
# automatically update ylim of ax2 when ylim of ax1 changes.
fig , ax =plt.subplots()
ax.boxplot([users,IPs], vert=True,patch_artist=True)
ax.set_yscale('log')
# add x-tick labels
plt.setp([ax], xticklabels=['Users', 'IPs'])
ax.set_ylabel('PUTs')
ax.grid(True)
plt.show()


