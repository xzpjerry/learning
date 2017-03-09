if __name__ == '__main__':
    with open('io_try.py', 'r') as f:
        #print(f.read(1024)) # 1024 bytes
        #print(f.read()) # all at once
        #print(f.readlines()) # read all and divide them into lines 
        for line in f.readlines():
            print(line.strip()) # delete every line's '\n'
            #print(line)
    
    try:
        with open('io_write_try.py', 'r') as f:
            contents = f.read() + '\n'
    except:
        with open('io_write_try.py', 'w') as f:
            contents = 'Hello!'
            f.write(contents)
    finally:
        print(contents)


    from io import StringIO
    f = StringIO('Hello\n, \nIm a str')
    print(f.getvalue())
    tmp_str = f.readlines()
    for line in tmp_str:
        print(line.strip())


    from io import BytesIO
    f = BytesIO()
    f.write('这是一句 byte'.encode('utf-8'))
    print(f.getvalue())