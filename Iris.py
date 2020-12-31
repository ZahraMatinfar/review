import codecs
import csv
import urllib.request
from ListClass import ExtendedList

url = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"
stream = urllib.request.urlopen(url)
csv_file = csv.reader(codecs.iterdecode(stream, 'utf-8'))
iris_list = []
for row in csv_file:
    iris_list.append(ExtendedList(row))

iris_list = iris_list[1:]
iris_list2=[]
for obj in iris_list:
    temp_list = []
    iterator = iter(ExtendedList.next_val(obj.lst))
    while True:
        try:
            temp_list.append(next(iterator))
        except StopIteration:
            break
    iris_list2.append(ExtendedList(temp_list))

