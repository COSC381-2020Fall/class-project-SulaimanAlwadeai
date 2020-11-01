import sys
from whoosh import scoring
from whoosh.index import open_dir
from whoosh.qparser import QueryParser

def performQuery(queryTerm, pageNum, itemsPerPage):
    ix = open_dir("index_dir")
    with ix.searcher(weighting=scoring.Frequency) as searcher:
        queryParser = QueryParser("description", ix.schema)
        query = queryParser.parse(queryTerm)
        results = searcher.search_page(query, pageNum, pagelen=itemsPerPage)

        resultsList = []
        for i in results:
            resultsDict ={
                "Title": i['title'],
                "Description": i['description'],
                "Link": "https://www.youtube.com/watch?v=%s" % i['id'],
                "Score": i.score
            }
            resultsList.append(resultsDict)
            
        return resultsList, results.total, results.pagecount

if __name__ == '__main__':
    queryTerm = sys.argv[1]
    pageNum = int(sys.argv[2])
    itemsPerPage = int(sys.argv[3])
    performQuery(queryTerm, pageNum, itemsPerPage)
