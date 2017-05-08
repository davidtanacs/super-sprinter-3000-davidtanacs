from flask import Flask, render_template, request
from jinja2 import *
import os
import csv
import sys
import html
app = Flask(__name__)


def read():
    table = []
    with open("/home/tanacs/super-sprinter-3000-davidtanacs/stories.csv", "r") as data:
        for line in data:
            lines = line.replace("\n", "")
            words = lines.split(',')
            table.append(words)
    return table


def add_ID(table):
    ID = len(table)
    for story in table:
        if ID == story[0]:
            ID += 1
    return str(ID)


@app.route('/')
def root():
    return render_template('list.html', title=titles)

titles = ["Add new Story", "Edit Story"]


@app.route('/new_story', methods=['GET', 'POST'])
def add_new():
    return render_template('form.html', title=titles)


@app.route('/add_new', methods=['GET', 'POST'])
def new_story():
    table = read()
    new_id = add_ID(table)
    name = request.args.get('name')
    story = request.args.get('story')
    criteria = request.args.get('criteria')
    value = request.args.get('value')
    estimation = request.args.get('estimation')
    status = request.args.get('status')
    storylist = [new_id, name, story, criteria, value, estimation, status]
    with open('/home/tanacs/super-sprinter-3000-davidtanacs/stories.csv', 'a') as f:
        for i in storylist:
            f.writelines(i + ",")
        f.write('\n')
    return render_template('list.html', title=titles)


@app.route('/', methods=['GET', 'POST'])
def updated_list():
    with open('/home/tanacs/super-sprinter-3000-davidtanacs/stories.csv', 'r') as f:
        stories = [word for line in f for word in line.split(",")]
    return render_template('list.html', stories=stories)


if __name__ == "__main__":
    app.run(debug=True) 