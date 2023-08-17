import keras
import pandas as pd
from celery import shared_task
from main_app.models import User, Books, Ratings
from ml.main import training, predict


@shared_task
def create_model(db_path, model_path):
    df = pd.DataFrame(o.__dict__ for o in Ratings.objects.all())
    df.to_csv(db_path)
    dataset = pd.read_csv(db_path)
    dataset.sort_values(by='book_id', inplace=True)
    model = training(dataset)
    model.save(model_path)


@shared_task
def use_model(user_id, db_path, model_path):
    user = User.objects.get(id=user_id)
    dataset = pd.read_csv(db_path)
    model_loaded = keras.models.load_model(model_path)
    recomm_books = predict(dataset, model_loaded, user_id)
    user.recomm_books = ','.join(map(str, recomm_books))
    user.save()
