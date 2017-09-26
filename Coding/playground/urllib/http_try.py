from urllib import request


req = request.urlopen('http://www.google.com/')
req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30')
with request.urlopen(req) as f:
    print('Status: ', f.Status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:',f.read().decode('utf-8'))
