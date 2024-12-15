import requests

url = "https://www.sofascore.com/api/v1/odds/1/featured-events/football"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9,en-IN;q=0.8',
  'baggage': 'sentry-environment=production,sentry-release=8zhE7UmNBsMD0JOyyA4je,sentry-public_key=d693747a6bb242d9bb9cf7069fb57988,sentry-trace_id=8b19b6e2374c4fc697f114f7c2f5604e',
  'cache-control': 'max-age=0',
  'cookie': '_lr_retry_request=true; _lr_env_src_ats=false; _ga=GA1.1.1220924724.1734262350; gcid_first=d0e35183-e842-405b-b01b-7b202e8b03b5; __browsiSessionID=4f187f1e-2437-4af1-9bd4-11968b0a7d64&false&DEFAULT&in&desktop-4.35.632&false; __browsiUID=ac59e805-d6ee-4ca0-abcd-438015b9177f; __gads=ID=e4ab5cfbd3cce27a:T=1734262357:RT=1734262357:S=ALNI_MY_hoGwiKahK0tGGTNr3Do7rWojsQ; __gpi=UID=00000f91d8e332ce:T=1734262357:RT=1734262357:S=ALNI_MZkwQ4Isf-MRN6-0kAsnw7hJ0AJkA; __eoi=ID=88a4797ef37e86c4:T=1734262357:RT=1734262357:S=AA-AfjYNenbNhZGyCsXfq1vZveei; _awl=2.1734262357.5-63d255dd00e02cabc13bfb414fa93757-6763652d617369612d6561737431-0; FCNEC=%5B%5B%22AKsRol_yfMillMNVNMqDJ3GIi4LDJJMpIoyciv8SQj8MbocFOymFaJkbzzJxwi24r05DYVB_jEuPrTS3WCC6L5OwMV4KQsLhLjh0UpRm_lo4LWSkTVfZGGFcsZ2RtOkpkMp2YNtDA1CfatncFDr22SGxjcFKznaPFQ%3D%3D%22%5D%5D; __qca=P0-170652232-1734262351231; cto_bundle=DKUJ2V93QWR5aE44Rm91VyUyRkVwV2olMkJsJTJCMFNGcFMxb0hSdVV0aWFUamNUOVZ6WXFQeDhZaHpPSlJsZGh0TW1ra3V2MEg2T3J6YmlNaHVHZk1ncnVFbllJTWRlRXBPZDJhT3JDQmFpV3dRckM2ckdmVGk1WHJBbXUlMkZFTjl6UVJCRzhUU1VKdDFtWjZYdE5XVmJ5NFRCUlFoaks0USUzRCUzRA; _ga_HNQ9P9MGZR=GS1.1.1734262349.1.0.1734262411.60.0.0',
  'if-none-match': 'W/"96aa91fa9a"',
  'priority': 'u=1, i',
  'referer': 'https://www.sofascore.com/',
  'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'sentry-trace': '8b19b6e2374c4fc697f114f7c2f5604e-a6ebfc88217108a5',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
  'x-requested-with': 'cdad2c'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
