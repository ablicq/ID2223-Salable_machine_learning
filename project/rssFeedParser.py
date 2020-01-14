#!/usr/bin/env python3

import feedparser as fp

feedsToParse = ["https://www.buzzfeed.com/" + s + ".xml" for s in [
    "index",
    "quizzes",
    "lol",
    "wtf",
    "fail",
    "win",
    "omg",
    "animals",
    "books",
    "celebrity",
    "comics",
    "cute",
    "nifty",
    "tvandmovies",
    "food",
    "tech",
    "geeky",
    "health",
    "lgbt",
    "reader",
    "rewind",
    "sports",
    "trashy",
    "bringme",
    "world"
    ]]

feedsToParse.append("https://feeds.feedburner.com/CrackedRSS")
feedsToParse.append("https://feeds.feedburner.com/viralstories/wuOI")

outFile = "titles.txt"

with open(outFile, 'a+') as f:
    for feedURI in feedsToParse:
        feed = fp.parse(feedURI)
        for entry in feed.entries:
            f.write(entry.title)
            f.write("\n")
