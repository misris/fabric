import getpass
from fabric import SerialGroup as Group
from fabric import Connection, Config

def whoami(c):
    result = c.run('whoami')
    # >> (usrname)
    print(result.connection.host)
    # >> localhost
    print(result.exited)
    # >> 0

def sudo_whoami(c):
    c.sudo('whoami', hide='stderr')
    # >> root

# input sudo pass just one time
sudo_pass = getpass.getpass("sudo password: ")
# store sudo pass
config = Config(overrides={'sudo': {'password': sudo_pass}})

# connect multiple servers
for connection in Group('localhost', 'localhost', user='misris', port=2222, config=config):
    # pass Connection obj on to method
    whoami(connection)
    sudo_whoami(connection)
