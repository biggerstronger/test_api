import requests

API_KEY = 'NWVjOTRhMzUtODU1MC00ZmFhLWExMjQtOWJiNmIxOGNkNTY4Ojc1ZGM1YTZhYjgyMTRiNjFhY2I3OTE5NzFlZTgwZjQ5'
AUTH_URL = 'https://developers.lingvolive.com/api/v1.1/authenticate'
# APP_KEY = 'ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmxlSEFpT2pFMk5EY3lOVFF4TmpBc0lrMXZaR1ZzSWpwN0lrTm9ZWEpoWTNSbGNuTlFaWEpFWVhraU9qVXdNREF3TENKVmMyVnlTV1FpT2pZeU1qTXNJbFZ1YVhGMVpVbGtJam9pTldWak9UUmhNelV0T0RVMU1DMDBabUZoTFdFeE1qUXRPV0ppTm1JeE9HTmtOVFk0SW4xOS55UndCZ3ctdERfVW1RVW9kcnFMbHhsemx4YllRcWp0VU9PejhMN0JONmhR'
ENG = '1033'
RU = '1049'

auth_header = {'Authorization': 'Basic ' + API_KEY}
auth = requests.post(AUTH_URL, headers=auth_header)
print(auth)
