import requests
import pandas as pd


data = pd.read_csv('LIME.csv')


def checker(row):
    phone = row['phone']
    resp = requests.get(url=f'https://ekapusta.com/partner/checkPhone/29950e94211c2/{phone}').json()
    if resp['phones'][0]['result'] == 'unexists':
        return True
    else:
        return False


data['status'] = data.apply(checker, axis=1)


data.to_csv('output.csv')
