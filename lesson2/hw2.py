import csv
with open('pythontvdi\lesson2\student.csv',"r",encoding="utf-8") as file:
    www = csv.DictReader(file)
    list1=[]
    lista=[]
    for i in www:
        print(i)
        list1.append(dict(i))
    print()
    for i in list1:
        if int(i['age']) > 22:
            print(i)
            lista.append(i)
with open('pythontvdi\lesson2\date2.csv',"w",encoding="utf-8") as file:
    # wwww = csv.writer(file)
    # for item in list:
    #  wwww.writerow(item)
    wwww = csv.writer(file)
    for i in lista:
        wwww.writerow([i])