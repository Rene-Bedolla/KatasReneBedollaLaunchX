def main():
    try:
        configuration = open('config.txt')
    except OSError as err:
        if err.errno == 2:
            print("Could't find the config.txt")
        elif err.errno == 13:
            print("Found config.txt but it is a directory, could't read it")

if __name__ == '__main__':
    main()
