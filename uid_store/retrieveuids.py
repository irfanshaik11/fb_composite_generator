
import re
pattern = re.compile(r"(\{id:\"\d*\",name)")


ids = set()
for i in range(1): # repeats the operation 1 times
    for i, line in enumerate(open('friendslist' + str(i+1) + '.txt','r')):
        for match in re.finditer(pattern, line):
            ids.add(match.groups()[0].split("\"")[1])
            # print('Found on line %s: %s' % (i+1, match.groups()))
            #
print("found " + str(len(ids)) + " ids")
print(ids)