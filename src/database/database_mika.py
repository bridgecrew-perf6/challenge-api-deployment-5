import datetime
import pandas as pd
import pickle
from pymongo import MongoClient
from mongoengine import *


client = MongoClient('localhost', 27017)
#client = MongoClient('mongodb://localhost:27017')

db = client.pymongo_test
#db = client['pymongo_test']

print(db)


# posts = db.posts
# post_data = {
#     'title': 'Python and MongoDB',
#     'content': 'PyMongo is fun, you guys',
#     'author': 'Scott'
# }
# result = posts.insert_one(post_data)
# print('One post: {0}'.format(result.inserted_id))

# post_1 = {
#     'title': 'Python and MongoDB',
#     'content': 'PyMongo is fun, you guys',
#     'author': 'Scott'
# }
# post_2 = {
#     'title': 'Virtual Environments',
#     'content': 'Use virtual environments, you guys',
#     'author': 'Scott'
# }
# post_3 = {
#     'title': 'Learning Python',
#     'content': 'Learn Python, it is easy',
#     'author': 'Bill'
# }
# new_result = posts.insert_many([post_1, post_2, post_3])
# print('Multiple posts: {0}'.format(new_result.inserted_ids))


# bills_post = posts.find_one({'author': 'Bill'})
# print(bills_post)

# scotts_posts = posts.find({'author': 'Scott'})
# print(scotts_posts)


# for post in scotts_posts:
#     print(post)


#-----------------------------------------------------------

connect('mongoengine_test', host='localhost', port=27017)


class Post(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)
    author = StringField(required=True, max_length=50)
    published = DateTimeField(default=datetime.datetime.now)


post_1 = Post(
    title='Sample Post',
    content='Some engaging content',
    author='Scott'
)
# post_1.save()       # This will perform an insert
# print(post_1.title)
# post_1.title = 'A Better Post Title'
# post_1.save()       # This will perform an atomic edit on "title"
# print(post_1.title)


# post_2 = Post(content='Content goes here', author='Michael')
# post_2.save()


#---------------------------------------------------------------

class Estate(Document):

    immoweb_id = IntField()
    price = FloatField()
    is_house = FloatField()
    subtype_property = StringField()
    area = FloatField()
    num_rooms = FloatField()
    postal_code = FloatField()
    region = StringField()
    garden = FloatField()
    garden_area = FloatField()
    terrace = FloatField()
    terrace_area = FloatField()
    num_facades = FloatField()
    building_state = StringField()
    equipped_kitchen = FloatField()
    furnished = FloatField()
    open_fire = FloatField()
    swimming_pool = FloatField()
    land_area = FloatField()


#------------------------------------------------------


# df = pd.DataFrame(pd.read_csv("src/model/dataset.csv"))
# data_dict_records = df.to_dict(orient='records')

# print(df.head(5))
# print("data_dict_records",data_dict_records[0])

# db = client.estate_test

# estate = db.estate

# result = estate.insert(data_dict_records)
# print(result)

#-------------------------------------------------------------------


properties_df = pickle.load(open('src/database/properties_df.pickle', 'rb'))
properties_df['immoweb_id'] = properties_df.index

data_dict_records = properties_df.to_dict(orient='records')

db = client.estate

estate = db.estate

result = estate.insert(data_dict_records)
data_db = estate.find()
print(data_db[5])




