# Apple Music Replay Data Tracker
**Apple Music Replay** is a weekly updated playlist that tracks and ranks songs based on amount of listening every year.
It was introduced by Apple Music, a music streaming platform by Apple, in 2019 as a year-end playlist feature like 
Spotify Wrapped which is generated every year.

**This is not an automatic tracker** as there are immeasurable obstacles to overcome
automatic webscraping such as two-factor authentication (remote Apple Music) and OS navigation (local iTunes). 
I came to another solution using Apple MusicKit to develop this tracker, but it costs a subscription price so I thought 
it would be better doing a manual export (3-click only) and running a batch script, which came at a no cost solution.

Therefore, I have to manually export a data file of the playlist, which updates every weekend. On this repository are
folders by week, each of them includes:
* a csv file (delimited by a tab). Because UTF-16 is not supported, some of the characters in the list will not be properly formatted.
  
* a table in markdown file for viewing purposes.

I only include 6 fields in this project (no. id, song title, artist, album title, genre, and song length) for simplicity.