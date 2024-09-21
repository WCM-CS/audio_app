# audio_app

Steps
- Jupyter notebook file used to convert youtube videos into mp4 file
- mongo_upload script interacts with mongodb instance and stored mp4 data in db via gridfs.
- Optimizations: Due to poor speed the changes made to the app are to use aac files rather than mp4 for storing just the audio data. Also making indices per each field will help with loookup speeds, besides from that cachng the metadata for the gridfs files will help with loookup speed and extraction also. Using python to push the files proed to be too slow so using go for the api may be a better idea. GO will also prove useful for caching the data on app initialization via concurrent queries to the database.
