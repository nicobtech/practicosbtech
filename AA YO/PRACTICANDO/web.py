import requests
r = requests.get("https://macowins-server.herokuapp.com/prendas/1")
r.json()
r.headers