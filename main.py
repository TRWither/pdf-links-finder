from lib import getpath, findlinks

def main():
    path = getpath()
    if path:
        findlinks(path)

if __name__ == "__main__":
    main()