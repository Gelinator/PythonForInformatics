count = 0
data2 = list()

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
        mysock.close()

        for i in data:
            count += 1
            data2 = data2.append(i)
            if count == 3000:
        print data2
            break
    except:
        print "Please enter a valid URL including the http://"