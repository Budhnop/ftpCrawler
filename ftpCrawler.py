#usage ftpCrawler.py "hostname"

from ftplib import FTP, error_perm
import sys

def traverse(ftp, depth=0):
    if depth > 10:
        return ['depth > 10']
    level = {}
    for entry in (path for path in ftp.nlst() if path not in ('.', '..')):
        try:
            if len(entry.split(".")) > 1:
                print(ftp.pwd(), entry)
            ftp.cwd(entry)
            level[entry] = traverse(ftp, depth+1)
            ftp.cwd('..')
        except error_perm:
            level[entry] = None
    return level


def main():
    ftp = FTP(sys.argv[1])
    ftp.login()

    out = traverse(ftp)
    print(out)
    with open("output.txt", "w") as output_file:
        output_file.write(str(out))


if __name__ == '__main__':
    main()
