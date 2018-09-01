from fabric import Connection
c = Connection(host='localhost', user='misris', port=2222)
c.run('uname -a')
