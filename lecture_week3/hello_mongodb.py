from pymongo import MongoClient
from pprint import pprint
client = MongoClient('localhost', 27017)
db = client.dbsparta
# web service 당 database 를 가지고
# database는 collection 으로 분류하고 collection은 dict로 구성
# 서버 입장에서 데이터베이스에 요청을 하기 때문에
# 서버가 client --> MongoClient 사용하여 요청을 날림
"""
db.users.insert_one({'name': 'bobby', 'age':21})
db.users.insert_one({'name':'kay','age':27})
db.users.insert_one({'name':'john','age':30})
"""
all_users = list(db.users.find())
pprint(all_users)

same_ages = list(db.users.find({'age': 21}))

user = db.users.find_one({'age': 21})
print(user)

# 수정할 조건, 수정할 내
db.users.update_many({'name': 'bobby'},{'$set': {'age':19}})
user = db.users.find_one({'name': 'bobby'})
print(user)

