import requests

patient_id = 2
url = "tesla.iem.pw.edu.pl:9080/v2/monitor/2"
df = requests.get(f"http://tesla.iem.pw.edu.pl:9080/v2/monitor/{patient_id}")
df = df.json()
d = df["trace"]["sensors"]


# print(type(url))
print(df)
print(d)

