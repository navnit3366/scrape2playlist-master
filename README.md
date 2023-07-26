[dg] - DigitalGangster.com

** must edit cfg.py before running **

dg_scrape2playlist - for dg's 6um.
Turning music threads into youtube playlists.


Three files: 

dg_yt_scraper.py - iterates through a 6um thread, 
capturing every posted youtube video url.

strip_dupes.py - optional. strips dupes from the
list generated above. 

yt_playlist_creator.py - after manually creating a
youtube playlist, this program will
automatically add videos from a list
to that playlist. takes about 15 
seconds per video, can take a while.


Notes:

yt_playlist_creator will occasionally raise an exception
(error out). I seemed to get this every 100 videos or so,
I think it was due to the page occasionally taking too 
long to load. You will have to manually remove urls from 
the url list, then restart the program. Sorry!

Written with python3.

6um runs on discourse forum software, this should work
on similar boards as well.

Thanks for looking.
