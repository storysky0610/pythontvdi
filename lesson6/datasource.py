import requests
def get_sitenames()->list[str]:
    url = 'https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON'
    try:
        response = requests.get(url)
        response .raise_for_status()
        data = response.json()
    except Exception as e:
        print(e)
    else:
        sitenames = set()
        for item in data['records']:
            sitenames.add(item['sitename'])
        sitenames = list(sitenames)
        return sitenames
