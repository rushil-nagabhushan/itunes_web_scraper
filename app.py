from flask import Flask, app, render_template, Response, request, redirect, url_for
import requests
from scraper import SingAlong

class WebInterface:
    # initialize flask
    app = Flask(__name__)

    # home page that renders html template on which random button and text entry reside
    @app.route('/', methods=['GET', 'POST'])
    def index():
        print(sa.top_100)
        return render_template("index.html", top_100_list = sa.top_100)

    # route for random selection of song for Flask app
    @app.route('/random', methods=['GET', 'POST'])
    def random_click():
        if request.method == 'POST':
            if request.form.get('random_button') == 'Random Song Select':
                #list_songs = sa.scrape_itunes()
                
                song_name = sa.return_random(sa.top_100_lyrics)
                link = sa.search_youtube(song_name)
                sa.open_link(link) 
        return render_template("index.html", top_100_list = sa.top_100)


    # create route function for text entry
        # needs to receive user input, check if input text is present in top 100
        # if present: process normally (might need to make separate function) and search up link
        # if not: output message saying song is not currently present in today's top 100.
    @app.route('/search', methods=['GET', 'POST'])
    def song_search():
        search_str = request.form.get('textbox')
        #if search_str.lower() in (song.lower() for song in sa.top_100):
        if any(search_str.lower() in song.lower() for song in sa.top_100):
            link = sa.search_youtube(search_str + ' lyrics')
            #print(link)
            sa.open_link(link)
        return render_template("index.html", top_100_list = sa.top_100)

if __name__ == '__main__':
    wi = WebInterface()
    sa = SingAlong()
    wi.app.run(debug=True, port=5000)
