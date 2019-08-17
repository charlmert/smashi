import codecs

# safely convert bytes to string
def bytesToString(obj):
    return codecs.decode(str(obj).encode('utf-8', errors='ignore'), errors='ignore')
