
if __name__ == '__main__':
    num = 0
    text_to_write = ''
    for i in range(10000):
        text_to_write = f"{text_to_write}potatoe\n"
    while True:
        num = num + 1
        f = open(f"the-file{num}.txt", "w+")
        f.write(text_to_write)
        f.close()