# adapted from https://git.styrion.net/iteas/iteas-tools/blob/master/proxmox/proxmox_install_PVE5.py

def check_filesystem():
    try:
        zfsc = run_cmd_output('zfs list')
        if zfsc[0] == 1 or zfsc[2].find('no datasets') != -1:
            return 'standard'
        else:
            return 'zfs'
    except:
        return 'standard'


def find_line(file, findstr, encoding='utf-8'):
    fp = open(file, "r+", encoding=encoding)
    for line in fp.readlines():
        if line.find(findstr) != -1:
            return True

    fp.close()
    return False

def replace_line(file, findstr, replstr, encoding='utf-8'):
    fp = open(file, "r+", encoding=encoding)
    buf = ""
    for line in fp.readlines():
        if line.find(findstr) != -1:
            line = replstr + "\n"

        buf += line

    fp.close()
    fr = open(file, "w+", encoding=encoding)
    fr.write(buf)
    fr.close()

def create(file, str):
    fr = open(file, "w+")
    fr.write(str + "\n")
    fr.close()

def append(file, str):
    fr = open(file, "a")
    fr.write(str + "\n")
    fr.close()

def touch(file):
    with open(file, 'a'):
        os.utime(file, None)
