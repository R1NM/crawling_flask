from flask import Flask, render_template
app = Flask(__name__)

import crawling


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/about')
def about():
    return "This is music chart crawling web-service"


@app.route('/billboard')
def billboard():

    song_list = crawling.billboard()

    return render_template("crawl.html",chart_name="BILLBOARD",song=song_list)

@app.route('/melon')
def melon():

    song_list = crawling.melon()

    return render_template("crawl.html",chart_name="MELON",song=song_list)


if __name__ == '__main__':
    app.run()
