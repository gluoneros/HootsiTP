from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ['usuario1']
password = os.environ["usuario6"]
host = os.environ["127.0.0.1"]
database = os.environ["contactsdb"]

DATABASE_CONNECTION_URI = f'mysql://{user}:{password}@{host}/{database}'
print(DATABASE_CONNECTION_URI)
