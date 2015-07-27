from flask import Flask, render_template, redirect, request
app = Flask(__name__)

from data import add_entry, get_link

@app.route("/")
def home():
    return render_template('url_form.html')

@app.route("/add_new_very_long_url", methods=["POST"])
def add_url():
    long_url = request.form['long_url']
    short_url = request.form['short_url']
    if len(long_url) > 0:
        add_entry(short_url, long_url)
    return redirect('/')

@app.route("/<link>")
def go_to_url(link):

    return redirect(get_link(link))


if __name__ == "__main__":
    app.run(debug=True)
