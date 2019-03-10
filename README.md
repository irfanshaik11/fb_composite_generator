# Friendly

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Friendly overlays features from all your friends to create an image of what an average person in your friend group looks like.

Made for HackRU 2019.

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

### Benefits of the Project
There are limited size datasets available for research purposes that are properly tagged with personal data such as a user's age, gender, location as well as other metadata. This app will be released on Facebook as a game users could play to find out what their average friends look like, and the image data would be sent along with metadata tags would be collected in a database for use in research.

### Parts to the Project
  - Selenium Web Scraper
  - Facebook Graphs API 
  - OpenCV + CNN Face Overlayer
 
### Selenium Web Scraper
  - Facebook Graphs API does not allow the retrieval of user friend lists unless the app undergos review by Facebook. This workaround asks a user to enter their account and navigate to their Facebook Friends List so the app can retrieve user's friend's IDs.
 - The web scraper uses chrome binaries to open a webpage where the user navigates to list of friends
 - This list of friends is downloaded and stored

### Facebook Graphs API
  - Facebook profile photos are public domain so can be accessed by anyone as per Facebook Policy
  - The Graphs API interacts with a developer only API to download facebook profile images using a user's ID

#### OpenCV + CNN Face Overlayer
  - Using OpenCV, I use builtin libraries to estimate the user's facial pose
  - The user's facial pose is corrected and overlayed with images of all other friends
