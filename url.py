from flask import Flask, render_template, redirect, request
app = Flask(__name__)
from data import add_entry, get_link, valid_short_url, isValid, current_host, valid_long_url, generate_link


@app.route("/")
def home():
    nav = "Make the long URL much shorter!"
    return render_template('url_form.html', Nav = nav)


@app.route("/add_new_very_long_url", methods=["POST"])
def add_url():
    long_url = request.form['long_url']
    short_url = request.form['short_url']
    nav = "Here is your short link!"
    if valid_long_url(long_url):
        if valid_short_url(short_url):
            add_entry(short_url[len(current_host):], long_url)

        else:
            new_link = generate_link()
            short_url = current_host + new_link
            add_entry(new_link, long_url, new_link)
        return render_template("link_added.html", Nav = nav, short_link = short_url)


@app.route("/<link>")
def go_to_url(link):
    if isValid(link):
        return redirect(get_link(link))
    else:
        return render_template('not_available.html')


if __name__ == "__main__":
    app.run(debug=True)
