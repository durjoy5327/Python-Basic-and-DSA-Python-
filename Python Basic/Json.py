
"""book={}
book['Durjoy']={
    'Name':'Durjoy Barua',
    'Address': 'Chittagong',
    'Gender':'male'
}
book['Mehlaching']={
    'Name': 'Mehlaching Marma',
    'Address':'Dhaka',
    'Gender':'Female'
}

s= json.dumps(book)
with open ("sample.txt","w") as f:
    f.write(s)
"""
import json
with open('sample.txt','r') as f:
    s= json.load(f)
print(s)

for i in s:
    print(s[i])
