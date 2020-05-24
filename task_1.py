string = input("Введіть, будь ласка, ваше речення: \n")
string_list = string.split(" ")
string_dict = {}
count = []

for i in range(len(string_list)):
    count.append(string.count(string_list[i]))
    string_dict[string_list[i]] = count[i]

print(string_dict)


