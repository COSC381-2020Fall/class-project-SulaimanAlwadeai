import json
import asyncio
import config
# from googleapiclient.discovery import build

my_api_key = config.credentials['my_api_key'] # The API_KEY you acquired
my_cse_id = config.credentials['my_cse_id'] #The search-engine-ID I  created
my_search_topic = 'how to post in facebook' #The phrse that I  want to search in facebook 

async def google_search(search_term, api_key, cse_id, start_index, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, start=start_index, **kwargs).execute()
    await asyncio.sleep(5)
    return res['items']  

async def main():
    L = await asyncio.gather(
        google_search(my_search_topic, my_api_key, my_cse_id, 0, num=10),
        google_search(my_search_topic, my_api_key, my_cse_id, 11, num=10),
        google_search(my_search_topic, my_api_key, my_cse_id, 21, num=10),
        google_search(my_search_topic, my_api_key, my_cse_id, 31, num=10),
        google_search(my_search_topic, my_api_key, my_cse_id, 41, num=10),
        google_search(my_search_topic, my_api_key, my_cse_id, 51, num=10),
        google_search(my_search_topic, my_api_key, my_cse_id, 61, num=10),
        google_search(my_search_topic, my_api_key, my_cse_id, 71, num=10),
	google_search(my_search_topic, my_api_key, my_cse_id, 81, num=10),
	google_search(my_search_topic, my_api_key, my_cse_id, 91, num=10),
    )
    with open('google_search.json', 'w', encoding='utf-8') as f:
        json.dump(L, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
