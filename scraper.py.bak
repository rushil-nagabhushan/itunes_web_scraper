import requests
from bs4 import BeautifulSoup
import json
from youtube_search import YoutubeSearch
from random import randrange
import webbrowser
from flask import Flask, app, render_template, Response, request, redirect, url_for


class SingAlong:
# initialize flask
#
    # initialize the class with the headers (default) we will need later
    def __init__(self, 
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }):
        self.headers = headers
        # top_100 is a list of the top 100 songs, top_100_lyrics is a list of the top 100 songs with 'lyrics' appended
        self.top_100, self.top_100_lyrics = self.scrape_itunes()


    # function that scrapes iTunes top 100 in the US for random selection
    # URL is set by default in the function to point to iTunes top 100 list
    def scrape_itunes(self, url="https://music.apple.com/us/playlist/top-100-global/pl.d25f5d1181894928af76c85c967f8f31"):
        req = requests.get(url, self.headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        # convert soup to text
        text_soup = soup.prettify()
        # marker to denote the start of the json body to parse
        start = text_soup.find('{"@context"')
        # marker to denote the end
        end = text_soup.find("</script>",71137)
        # get list of songs in top 100
        song_list = text_soup[start:end].strip()
        # convert song list to json
        json_song_list = json.loads(song_list)
        # narrow down the json parsing for tracks only
        song_names = json_song_list['track']
        # create empty array in which to store song names
        lyric_list = []
        top_list = []
        # store song names in empty array
        for i in song_names:
            lyric_list.append(i['name'].replace('&amp;','&') + ' lyrics')
            top_list.append(i['name'].replace('&amp;','&'))

        return top_list, lyric_list

    def return_random(self, song_choice_list):
        # create and save random number for selection from list
        random_num = randrange(0,len(song_choice_list)-1)
        return song_choice_list[random_num]

    # function that obtains a search_term from scrape_itunes() and returns
    # a link to the video on youtube
    def search_youtube(self, search_term):
        # search for one randomly selected song name and stores resulting video data in variable
        search_result = YoutubeSearch(search_term, max_results=1).to_json()
        # converts search_result to json, narrows down json by looking at 'videos'
        json_result = (json.loads(search_result)['videos'])[0]
        # display title
        print(json_result['title'])

        # create, display, and return link
        link = 'https://www.youtube.com' + json_result['url_suffix']
        print(link)

        return link

    # open link returned from search_youtube() using webbrowser package
    def open_link(self, link):
        webbrowser.open(link)

if __name__ == '__main__':
    sa = SingAlong()
    #list_songs = sa.scrape_itunes()
    #sa.app.run(debug=True, port=5000)

    #song_name = sa.return_random(list_songs)
    #link = sa.search_youtube(song_name)
    #sa.open_link(link)


    

    