from pymongo import MongoClient
import gridfs
import os

client = MongoClient("mongodb://root:example@localhost:27019/")
database = client["audio_db"]
collection = database["audio_files"]

# Create a list of fdocument name fields
row_names = []
fs = gridfs.GridFS(database)

# Query to find all row names
docs = collection.find()

# iterate through file names storing to list
for doc in docs:
    row_names.append(doc['name'])
    
audio_files = [
    "Pure_Noise.mp4",
    "Gym_Phonk.mp4",
    "Lofi_Long.mp4",
    "Lofi_Short.mp4",
    "Best_Classical.mp4",
    "Dark_Classical.mp4"
]

for row_name, file in zip(row_names, audio_files):
    temp = os.path.join("audio", file)
    
    with open(temp, 'rb') as audio_file:
        file_id = fs.put(audio_file, filename=temp, contentType="audio/mp4")
        
        collection.update_one(
            {'name': row_name},
            {'$set': {'grid_data': file_id}}
        )

