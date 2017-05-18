import telnetlib
import logging
import sys

def main():
    try:
        host = sys.argv[1]
        user = sys.argv[2]
        passwd = sys.argv[3]
    except:
        logging.warn("No parameters passed")
        _print_help()

def _print_help():
    usage = "Usage: {} <host> <user>".format(sys.argv[0])
    print(usage)
    return 1

def connect(host,port,user,passwd):
    logging.debug('entering connect function')
    try:
        t = telnetlib.Telnet(host,port)
        t.connect()
    except:
        logging.error('Unable to connect to {} on port {}'.format(host,port))
        return 1
    try:
        t.read_until(b'Username:')
        t.write(b'{}'.format(user)+b'\n')
    except:
        logging.error('unable to pass username')

if __name__ == "__main__":
    main()

