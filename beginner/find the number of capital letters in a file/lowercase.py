with open("text.txt") as file:
    count = 0
    text = file.read()
    for i in text:
        if i.islower():
            count += 1

    print(count)