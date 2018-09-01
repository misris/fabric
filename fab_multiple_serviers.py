from fabric import Connection, Config
from fabric import SerialGroup as Group

# create group of remote servers
group = Group('localhost', 'localhost', user='misris', port=2222)

# apply commands to multiple servers
group.run('whoami')
group.run('uname -a')

# return GroupResult obj
results = group.run('whoami')

# show specific log
for connection, result in results.items():
    print("{0.host}: {1.stdout}".format(connection, result))
