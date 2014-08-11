# -*- coding: utf-8 -*-
# all the imports
from flask import request, redirect, url_for,\
    render_template
from apps import app
from database import Database

dataStorage = Database()


@app.route('/', methods=['GET', 'POST'])
def show_entries():
    entries = dataStorage.out()
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    storage = {}
    storage['id'] = dataStorage.newid()
    storage['title'] = request.form['title']
    storage['contents'] = request.form['contents']
    storage['url'] = request.form['url']
    storage['time'] = dataStorage.timezone()
    storage['likecount'] = 0
    dataStorage.put(storage)
    return redirect(url_for('show_entries'))


@app.route('/del/<key>', methods=['GET'])
def del_entry(key):
    dataStorage.delete(key)
    return redirect(url_for('show_entries'))


@app.route('/like/<key>', methods=['GET'])
def like_entry(key):
    storage = dataStorage.select(key)
    storage['likecount'] += 1
    dataStorage.update(key, storage)
    return redirect(url_for('show_entries'))


@app.route('/dislike/<key>', methods=['GET'])
def dislike_entry(key):
    storage = dataStorage.select(key)
    storage['likecount'] -= 1
    if storage['likecount'] < 0:
        storage['likecount'] = 0
    else:
        dataStorage.update(key, storage)
    return redirect(url_for('show_entries'))


@app.route('/edit/<key>', methods=['GET', 'POST'])
def edit_entry(key):
    entry = dataStorage.select(key)
    dataStorage.delete(key)
    return render_template('edit_entries.html', entry=entry)


@app.route('/edit/page', methods=['POST'])
def edit_page():
    storage = {}
    storage['id'] = request.form['edit_id']
    storage['title'] = request.form['edit-title']
    storage['contents'] = request.form['edit-contents']
    storage['url'] = request.form['edit-url']
    storage['time'] = dataStorage.timezone()
    storage['likecount'] = 0
    dataStorage.put(storage)
    return redirect(url_for('show_entries'))


@app.route('/top3', methods=['GET', 'POST'])
def top3():

    return render_template('top3.html', entries=entries)
