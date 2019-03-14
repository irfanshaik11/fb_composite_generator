# Friendly

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Friendly overlays features from all your facebook friends to create an image of what an average person in your friend group looks like.

Best Solo Hack Commended in HackRU 2019.

### Installation

Friendly requires [OpenCV](https://opencv.org/) v3 to run.

Install the dependencies and start the program.

```sh
$ mkdir friendly
$ cd friendly
$ git clone
$ pip install -r requirements.txt
$ python run.py
```

### Parts to the Project
  - Selenium Web Scraper
  - Facebook Graphs API 
  - OpenCV + CNN Face Overlayer
 
### Selenium Web Scraper
  - Facebook Graphs API does not allow the retrieval of user friend lists unless the app undergoes review by Facebook. This workaround asks a user to enter their account and navigate to their Facebook Friends List so the app can retrieve user's friend's IDs.
 - The web scraper uses chrome binaries to open a webpage where the user navigates to list of friends
 - This list of friends is downloaded and stored

### Facebook Graphs API
  - Facebook profile photos are public domain so can be accessed by anyone as per Facebook Policy
  - The Graphs API interacts with a developer only API to download facebook profile images using a user's ID

#### OpenCV + CNN Face Overlayer
  - Using OpenCV, I use builtin libraries to estimate the user's facial pose
  - The user's facial pose is corrected and overlayed with images of all other friends
