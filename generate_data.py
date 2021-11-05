import base64


def demo(path_for_read, path_for_write):
    with open(path_for_read, 'rb')as rf:
        data = rf.read()
        encode_data = base64.b64encode(data)
        with open(path_for_write, 'wb')as wf:
            wf.write(encode_data)


if __name__ == '__main__':
    path1 = ''
    path2 = ''
    demo(path1, path2)
