import  sqlite3
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

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

users =  [ (_id, _count,'user') for (_id, _count) in c]


c.execute(
        """ SELECT IP , count(*)
            FROM logs
            WHERE user == 'anonimo'
            GROUP BY IP
            ORDER BY 2 DESC
    """)

IPs = [(_id, _count,'IP') for (_id, _count) in c]



df_users = pd.DataFrame(users, columns= ['id','count','category'])
df_IPs = pd.DataFrame(IPs, columns= ['id','count','category'])

df_all = pd.concat([df_users, df_IPs])

print df_all.groupby('category').describe()

print ttest_ind(df_users['count'], df_IPs['count'])
# Save (commit) the changes
#conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
