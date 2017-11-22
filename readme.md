## anirandomise
![](http://i.imgur.com/miiFN0S.png)

![](http://i.imgur.com/YMBm9rj.png)

- randomly tries to run a file in the folder where it is placed with the file's default program
- tries to clean up file names to group similar named files together - name clean up regex is based off video release titles, so recommended usage is for randomised video playing (i.e. multiple episodes of a video will not increase chances of that one appearing, and only the earliest unwatched episode will be chosen)
- ignores directories
- requires pretty latest python probably

### new feature - logging
![](https://i.imgur.com/f0YMb74.png)
- the script will now create a log file named after itself except with a .log file extension
- the script ignores files that have its name, so the log will not be opened by the script
- the log file will detail what file choices were made