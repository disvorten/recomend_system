from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split
from keras.layers import Input, Embedding, Flatten, Dot, Dense
from keras.models import Model
import numpy as np
import sqlite3

BASE_DIR = Path(__file__).resolve().parent.parent


def training(dataset):
    train, test = train_test_split(dataset, test_size=0.3, random_state=42)
    n_users = len(dataset.user_id.unique())
    n_books = len(dataset.book_id.unique())
    book_input = Input(shape=[1], name="Book-Input")
    book_embedding = Embedding(n_books + 1, 5, name="Book-Embedding")(book_input)
    book_vec = Flatten(name="Flatten-Books")(book_embedding)
    user_input = Input(shape=[1], name="User-Input")
    user_embedding = Embedding(n_users + 1, 5, name="User-Embedding")(user_input)
    user_vec = Flatten(name="Flatten-Users")(user_embedding)
    prod = Dot(name="Dot-Product", axes=1)([book_vec, user_vec])
    model = Model([user_input, book_input], prod)
    model.compile('adam', 'mean_squared_error')
    model.fit([train.user_id, train.book_id], train.rating, epochs=5, verbose=1)
    return model


def predict(dataset, model, user_id):
    book_data = np.array(list(set(dataset.book_id)))
    user = np.array([user_id for i in range(len(book_data))])
    predictions = model.predict([user, book_data])
    predictions = np.array([a[0] for a in predictions])
    recommended_book_ids = (-predictions).argsort()
    # print(recommended_book_ids)
    # books = pd.read_csv('C:/Users/vorto/Desktop/project/recomend_system/main_app/data_for_ml/books.csv')
    # return books[books['id'].isin(recommended_book_ids)]
    return recommended_book_ids[:6]


import psycopg2

from sqlalchemy import create_engine


def To_DB(dataset, name):
    # conn = sqlite3.connect('C:/Users/vorto/Desktop/project/recomend_system/db.sqlite3')
    # dataset.to_sql(name, conn, if_exists='append', index=False)
    # conn.close()
    engine = create_engine('postgresql://postgres:SWeets_47@localhost:5432/postgres')
    dataset.to_sql(name, engine, if_exists='replace', index_label='id')


if __name__ == '__main__':
    dataset = pd.read_csv('data_2/ratings.csv')
    books = pd.read_csv('data_2/books.csv',
                        usecols=['book_id', 'books_count', 'isbn', 'authors', 'original_publication_year',
                                 'title', 'language_code', 'average_rating', 'image_url', 'small_image_url'])
    # print(books)
    # To_DB(dataset, 'ratings')
    # To_DB(books, 'main_app_books')
    # model = training(dataset)
    # books = predict(dataset, model, 1)
    # To_DB(books, '5 recommendations for user 1')
    # To_DB(dataset, 'main_app_ratings')
