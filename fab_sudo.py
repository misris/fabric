import getpass
from fabric import Connection, Config

# input sudo pass just one time
sudo_pass = getpass.getpass("sudo password: ")
# store sudo pass
config = Config(overrides={'sudo': {'password': sudo_pass}})

# connect remote server with config
c = Connection(host='localhost', user='misris', port=2222, config=config)

# not need to type sudo pass everytime
c.sudo('whoami', hide='stderr')
c.sudo('uname -a', hide='stderr')
