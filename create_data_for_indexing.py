from pathlib import Path
import json


paths = [str(x) for x in Path('./youtube_data').glob('**/*.json')]
results = []
for path in paths: 
  with open(path, 'r') as f:
    data = json.load(f)
    mydict = {'video_id': data['items'][0]['id'], 'title': data['items'][0]['snippet']['localized']['title'], 'description': data['items'][0]['snippet']['description']}
    results.append(mydict)

with open('data_for_indexing.json', 'w') as dump_file:
    json.dump(results, dump_file)
