import logging

from com.sanlap.bot.train.domain.model import TrainedModel, get_db

db = get_db()


def get_model_by_name(name, version=None, is_active=True):
    """
    Get the saved model
    :param name: the name of the model
    :param version: the model version
    :param is_active: indicates if the model is active or not
    :return: the path to the saved model
    """
    model = db.query(TrainedModel).filter_by(name=name, version=version, is_active=is_active).first()
    return model.path


def add_model(name, version, path, is_active=False):
    """
    Add the model to db
    :param name: the model name
    :param version: the model version
    :param path: the path to the saved model
    :param is_active: indicates if the model is active
    """
    model = TrainedModel(name=name, version=version, path=path, is_active=is_active)
    db.add(model)
    db.commit()
    logging.info(f'Added {model.name} to DB')
    logging.info(f'Current set of models hosted')
    logging.info(f'{[model for model in db.query(TrainedModel).all()]}')
