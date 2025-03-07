def write_to_file(list_of_elements):
    with open("sometext.txt", 'a', encoding="utf-8") as f:  
        text = " ".join(map(str, list_of_elements)) + "\n"  
        f.write(text)


write_to_file([12345, 56789, 90987654, "dfghjkl", "efrgf", 34, 34])


def write_to_file(list_of_elements):
    with open(r"D:\PP2\labs\lab6\dif-and-files\sometext.txt", 'a', encoding="utf-8") as f:
        text = " ".join(map(str, list_of_elements)) + "\n"
        f.write(text)

write_to_file([12345, 56789, 90987654, "dfghjkl", "efrgf", 34, 34])
