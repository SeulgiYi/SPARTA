print("hello,word")
a = 3
print(a)
b = a
print(b)
b = b + 1
print(b)

num1 = a*b
num2 = 99
print(num1, num2)

name = 'apple'
print(name)

is_number = True

a_list = list()
a_list.append(1)
a_list.append([2, 3])
print(a_list[0])
print(a_list[1])
print(a_list[1][0])

a_dict = dict()
a_dict = {'name': 'bob', 'age': 21}
a_dict['height'] = 178
print(a_dict)
print(a_dict['name'])
print(a_dict['age'])
print(a_dict['height'])

people = [{'name': 'bob', 'age': 20}, {'name': 'carry', 'age': 38}]
person = {'name': 'john', 'age': 7}
people.append(person)
print(people[0]['name'])
print(people[1]['name'])
print(people[2]['name'])
print(people[2]['age'])

def f(x):
    return 2*x+3
print(f(2))

def sum_all(a,b,c):
    return a+b+c

def mul(a,b):
    return a*b

def minus(a,b):
    return a-b


result = sum_all(1,2,3) + mul(10,10)
result2 = minus(mul(10,10), sum_all(1,2,3)) +1
print(result)
print(result2)

def oddeven(num):
    if num % 2 == 0:
        return True
    else:
        return False

def checkbob(name):
    if name == 'bob':
        return True
    else:
        return False

print(result, oddeven(result))
print(result2, oddeven(result2))
print('bob', checkbob('bob'))

def allsum(mylist):
    sum = 0
    for i in mylist:
        sum += i
    return sum

sth_list = [ i for i in range(10) ]
print(sth_list)
print(allsum(sth_list))

for person in people:
    print(person['name'] + ' / ' + str(person['age']))

def get_age(myname):
    for person in people:
        if person['name'] == myname:
            return person['age']
    return '해당하는 이름이 없습니다'

print(get_age('bob'))
print(get_age('kay'))

def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(3, prime(3))
print(4, prime(4))
print(4000, prime(4000))

import requests
import pprint

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
print(r)
rjson = r.json()
print(rjson)
pprint.pprint(rjson)
pprint.pprint(rjson['RealtimeCityAir']['row'][0])
print(rjson['RealtimeCityAir']['row'][0]['NO2'])

def get_index(gu_name):
    data = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
    jdata = data.json()
    gu_infos = jdata['RealtimeCityAir']['row']
    for gu_info in gu_infos:
        if gu_info ['MSRSTE_NM'] == gu_name:
            return gu_info['IDEX_MVL']
    return '옳지 않은 구 이름입니다'

print(get_index('중구'))
print(get_index('유성구'))
