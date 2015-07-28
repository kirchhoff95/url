# coding: utf-8

DATA_FILE = 'data.txt'
DATA_ENCODING = 'utf-8'

current_host = "http://127.0.0.1:5000/"
restricted_URLS = ["add_new_very_long_url", "non_available", "auto_generated_link"]


def load_entries_():
    with open(DATA_FILE, 'r', encoding=DATA_ENCODING) as data_file:
        return [eval(data_file.readline()), data_file.readline()]


def save_entries_(last):
    with open(DATA_FILE, 'w', encoding=DATA_ENCODING) as data_file:
        print(repr(entries_), file=data_file)
        print(last, file=data_file)


entries_, last_url = load_entries_()

def isAvailable_(short_):
    non_available = list(entries_.keys()) + restricted_URLS
    if short_ in non_available:
        return False
    return True


def isValid(link):
    return link in entries_.keys()


def valid_long_url(url):
    pr = "http://"
    if (len(url) <= len(pr)):
        return False
    elif url[:len(pr)] == pr:
        return True
    else:
        return False


def valid_short_url(url):
    isAvlb = isAvailable_(url)
    if len(url) <= len(current_host):
        return False and isAvlb
    elif url[:len(current_host)] == current_host:
        return True and isAvlb
    else:
        return False and isAvlb


def get_link(short_):
    if entries_.get(short_) == None:
        return '/'
    return entries_[short_]


def add_entry(short_, long_, last_ = 0):
    entries_[short_] = long_
    print ("Last URL is: " + last_url)
    save_entries_(last_)
    return


def generate_link():
    print (entries_, last_url)
    i = int(last_url)
    new_link = i + 1
    while True:
        if not isValid(str(new_link)):
            return str(new_link)
        else:
            new_link += 1