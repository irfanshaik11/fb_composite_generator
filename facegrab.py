from __future__ import print_function
import sys
import os
import requests
from datetime import datetime
from random import randint
import re


class Facegrab:
    def __init__(self):
        self.base_url = "http://graph.facebook.com/picture?id={}&width=800"
        self.sess = requests.Session()
        self.sess.headers.update({
            "User-Agent": "Facegrab v2"
        })

    @staticmethod
    def create_dir(prefix):
        dir_c = os.path.join(
            os.getcwd(),
            prefix,
#            datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            "myfriends"
        )
        try:
            os.makedirs(dir_c)
        except OSError as e:
            if e.errno != 17:
                pass
            else:
                print("Cannot create a folder.")
                exit
        return dir_c

    def getProfile(self, photoUrl, saveUrl):
        print(f"Downloading {photoUrl}.")
        response = self.sess.get(photoUrl)
        if response.headers["Content-Type"] == "image/gif":
            return
        with open(saveUrl, "wb") as f:
            f.write(response.content)
        return True

    def getImages(self, uids):
        sizeDataset = len(uids)
        _id = randint(1, int(1e4))
        photoCount = 0
        folder = self.create_dir("facegrab")
        while photoCount < sizeDataset:
            profile = self.getProfile(
                self.base_url.format(uids[photoCount]),
                f"{folder}/{_id}.jpg"
            )
            if profile:
                photoCount += 1
                _id += 1
            else:
                _id += 10    # Cannot understand the logic behind this.
        print(
            "\nFace Dataset created in facegrab folder."
            f"\nSize: {photoCount}"
        )
        print()
        return

def retrieve_uids():
    pattern = re.compile(r"(\{id:\"\d*\",name)")


    ids = set()
    for i in range(1): # repeats the operation 1 times
        for i, line in enumerate(open('friendslist' + str(i+1) + '.txt','r')):
            for match in re.finditer(pattern, line):
                ids.add(match.groups()[0].split("\"")[1])
    # print('Found on line %s: %s' % (i+1, match.groups()))
    #
    print("found " + str(len(ids)) + " ids")
    return list(ids)
if __name__ == "__main__":
    checks = [
        len(sys.argv) == 1,
#        sys.argv[1].isdigit()
#        int(sys.argv[1]) < int(1e7)
    ]
    
#    if not all(checks):
#        print("\nIncorrect arguments.")
#        print(
#              "Usage: python facegrab.py"
#              )



    uids = retrieve_uids()
    grabby = Facegrab()
#    grabby.getImages(int(sys.argv[1]), uids)
    grabby.getImages(uids)

