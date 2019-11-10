import joblib

from com.sanlap.bot.train.domain.query import get_model_by_name
from com.sanlap.bot.train.modeler.predictor import Predictor


def main():
    print('Enter the model name')
    model_name = str(input())
    print('Enter the model version')
    model_version = float(input())
    model_path = get_model_by_name(model_name, version=model_version)
    print(f'Model being used: {model_path}')
    model = joblib.load(model_path)
    print(f'Loaded model: {bool(model)}')
    predictor = Predictor(model)
    user_quit = False
    while not user_quit:
        print('User ->')
        user_input = str(input())
        bot_said = predictor.predict(user_input)
        print(f'{bot_said} <- Bot')
        print('Continue? [Y/N]')
        user_quit = str(input()).lower() == 'n'
    print('See you later!!')


if __name__ == '__main__':
    main()
