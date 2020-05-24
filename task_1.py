string = input("Введіть, будь ласка, ваше речення: \n")
string_list = string.split(" ")
string_dict = {}
count = []

for i in range(len(string_list)):
    count.append(1)
    if string_list[i] in string_list[(i + 1):]:
        count[i] += 1
    string_dict[string_list[i]] = count[i]

print(string_dict)


