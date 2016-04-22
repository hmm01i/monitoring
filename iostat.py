def log(level,msg):
    if level == "error":
        print "ERROR " + msg
    if level == "debug":
        print "DEBUG " + msg
    if level == "info":
        print "INFO " + msg
