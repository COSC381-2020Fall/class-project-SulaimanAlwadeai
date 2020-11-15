import os
import sys
from whoosh.index import create_in
import json
from whoosh.fields import Schema, TEXT, ID
from whoosh.analysis import StemmingAnalyzer

stem_analyzer = StemmingAnalyzer()
schema = Schema(id=ID(stored=True), title=TEXT(stored=True), description=TEXT(analyzer=stem_analyzer, stored=True))

if not os.path.exists("index_dir"):
    os.mkdir("index_dir")

ix = create_in("index_dir", schema)
writer = ix.writer()

with open('data_for_indexing.json') as f:
    youtube_data_array = json.load(f)
    for item in youtube_data_array:
        writer.add_document(id=item['id'], title=item['title'], description=item['description'])

writer.commit()
