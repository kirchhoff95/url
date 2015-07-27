# coding: utf-8

DATA_FILE = 'data.txt'
DATA_ENCODING = 'utf-8'


def load_entries_():
    with open(DATA_FILE, 'r', encoding=DATA_ENCODING) as data_file:
        return eval(data_file.read())


def save_entries_():
    with open(DATA_FILE, 'w', encoding=DATA_ENCODING) as data_file:
        print(repr(entries_), file=data_file)


entries_ = load_entries_()


def get_link(short_):
    if entries_.get(short_) == None:
        return '/'
    return entries_[short_]


def add_entry(short_, long_):
    entries_[short_] = long_
    save_entries_()
    return
