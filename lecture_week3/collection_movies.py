from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta
movies = list(db.movies.find())

title_to_search = '사운드 오브 뮤직'
target_movie = db.movies.find_one({'title': title_to_search})
target_point = target_movie['star']
print(target_point)

search_condition = {'star': target_point}
same_movies = list(db.movies.find(search_condition))
for movie in same_movies:
    print(movie['title'], movie['star'])

update_point = '0'
update_condition = { '$set': { 'star': update_point }}

db.movies.update_many(search_condition, update_condition)


