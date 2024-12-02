from urllib.parse import quote_plus
from pymongo import MongoClient
import pdb

username = quote_plus("skc3766")  # Replace with your actual username
password = quote_plus("Utr@1010")  # Replace with your actual password

connection_string = f"mongodb+srv://skc3766:{password}@cluster0.6c9ag.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
print(connection_string)
client = MongoClient(connection_string)
db = client['cosmo-cloud']
student_collection = db['students']
