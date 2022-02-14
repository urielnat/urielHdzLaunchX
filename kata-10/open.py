def main():
    try:
     open("mars.jpg")
    except (FileNotFoundError , OSError) as err:
     print("got a problem trying to read the file:", err)
     if err.errno == 2:
            print("Couldn't find the config.txt file!")
     elif err.errno == 13:
            print("Found config.txt but couldn't read it") 

if __name__ == '__main__':
    main()