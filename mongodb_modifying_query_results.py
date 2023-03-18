from mongo_conn import mongo_uri
from pprint import PrettyPrinter


printer = PrettyPrinter()
client = mongo_uri('atlas')
db = client['sample_training']


query = {'category_code': 'music'}
sort = 'name', 1
projection = {'name': 1}
cursor = db.companies.find(query, projection)
# in python you need to send the field name and the order
# 1 ascending | -1 descending
r = list(cursor.sort('name', 1))
printer.pprint(r)
