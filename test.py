import base64
s="UC7KOWVXWVNKNIC2XCXKHKK2W5NLBKNOUOSK3LNNVWW3E==="
s='\xa0\xbe\xa7Z\xb7\xb5Z\xa6\xa0Z\xb8\xae\xa3\xa9Z\xb7Z\xb0\xa9\xae\xa3\xa4\xad\xad\xad\xad\xad\xb2'
print(s)
m = ''
for i in s:
   x = ord(i) ^ 36
   x = x - 36
   m+= chr(x)
h = ''
for i in m:
   x = ord(i) - 25
   x = x ^ 36
   h+= chr(x)
print(h)