## Still looking for a way to handle urls with no http


while True:
    weburl = raw_input("Enter desired URL :")

    import socket

    cleanURL = weburl.split("/",)
    try:
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((cleanURL[2], 80))
        mysock.send('GET ' + weburl + ' HTTP/1.0\n\n')

        while True:
            data = mysock.recv(512)
            if ( len(data) < 1 ) :
                break
            print data;

        mysock.close()
        break
    except:
        print "Please enter a valid URL including the http://"