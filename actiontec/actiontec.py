import telnetlib
import logging
import sys
import getpass
import time

def _print_help():
    usage = "Usage: {} <host>[:port] <user>".format(sys.argv[0])
    print(usage)
    return 1

def _get_settings():
    """This is a private function to get parameters for connection
    :returns: tuple (host,port,user,passwd)

    """
    logging.debug('{} args were passed: {}'.format(len(sys.argv),sys.argv))

    try:
        full_host = sys.argv[1]
        print(full_host)
        if len(full_host.split(':')) == 2:
            host = full_host.split(':')[0]
            port = full_host.split(':')[1]
        else:
            host = full_host
            port = 23
        user = sys.argv[2]
        passwd = getpass.getpass()
    except:
        logging.warn("No parameters passed")
        _print_help()
        return 1
    logging.debug(host,port,user)
    return (host,port,user,passwd)

def main():
    """ This is the main function that we jump into
    if called from command line.
    This should be able to be imported
    and other functions can be called independently
    """

    host,port,user,passwd = _get_settings()
    router = connect(host,port,user,passwd)
    print(getRouterHelp(router).decode('ascii'))

def connect(host,port,user,passwd):
    logging.debug('entering connect function')
    try:
        t = telnetlib.Telnet(host,port)
    except:
        logging.error('Unable to connect to {} on port {}'.format(host,port))
        return 1
    try:
        t.read_until(b'Username:')
        t.write(user.encode('ascii')+b'\n')
        t.read_until(b'Password:')
        t.write(passwd.encode('ascii')+b'\n')
    except:
        logging.error('unable to pass username or password')
    return t

def getRouterHelp(connection):
    """TODO: Docstring for getHelp.
    :returns: returns output of help all command

    """
    connection.write(b'help all\n')
    time.sleep(2)
    output = connection.read_very_eager()
    return output


class router(object):
    """This is a class to group interactions with router"""
    def __init__(self, host, port, user, passwd):
        super(router, self).__init__()
        self.host, port, user, passwd = host, port, user, passwd
        self.connection = connect()

    def connect(self):
        logging.debug('entering connect function')
        try:
            t = telnetlib.Telnet(self.host,self.port)
        except:
            logging.error('Unable to connect to {} on port {}'.format(self.host,self.port))
            return 1
        try:
            t.read_until(b'Username:')
            t.write(self.user.encode('ascii')+b'\n')
            t.read_until(b'Password:')
            t.write(self.passwd.encode('ascii')+b'\n')
        except:
            logging.error('unable to pass username or password')
        return t

    def getHelp(connection):
        """TODO: Docstring for getHelp.
        :returns: returns output of help all command

        """
        connection.write(b'help all\n')
        time.sleep(2)
        output = connection.read_very_eager()
        return output

if __name__ == "__main__":
    main()

