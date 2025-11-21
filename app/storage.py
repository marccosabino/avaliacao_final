import pandas as pd
import os
import urllib.request
import zipfile

class Storage:
    def __init__(self, data_dir='data'):
        self.data_dir = os.path.abspath(data_dir)
        os.makedirs(self.data_dir, exist_ok=True)

        self.ratings_path = os.path.join(self.data_dir, 'ratings.csv')
        self.users_path = os.path.join(self.data_dir, 'users.csv')
        self.items_path = os.path.join(self.data_dir, 'items.csv')

    def ensure_data(self):
        if not os.path.exists(self.ratings_path):
            print("Baixando MovieLens 100k...")

            url = 'http://files.grouplens.org/datasets/movielens/ml-100k.zip'
            zip_path = os.path.join(self.data_dir, 'ml-100k.zip')

            urllib.request.urlretrieve(url, zip_path)

            with zipfile.ZipFile(zip_path, 'r') as z:
                z.extractall(self.data_dir)

            udata = os.path.join(self.data_dir, 'ml-100k', 'u.data')
            df = pd.read_csv(udata, sep='\t', header=None,
                             names=['user_id', 'item_id', 'rating', 'timestamp'])
            df[['user_id', 'item_id', 'rating']].to_csv(self.ratings_path, index=False)

            uitem = os.path.join(self.data_dir, 'ml-100k', 'u.item')
            try:
                items = pd.read_csv(uitem, sep='|', header=None, encoding='latin-1')
                items = items[[0, 1]]
                items.columns = ['item_id', 'title']
                items.to_csv(self.items_path, index=False)
            except:
                df_items = df[['item_id']].drop_duplicates().reset_index(drop=True)
                df_items['title'] = df_items['item_id'].astype(str)
                df_items.to_csv(self.items_path, index=False)

            df_users = df[['user_id']].drop_duplicates().reset_index(drop=True)
            df_users['name'] = df_users['user_id'].astype(str)
            df_users.to_csv(self.users_path, index=False)

    def load_ratings(self):
        return pd.read_csv(self.ratings_path)

    def load_users(self):
        return pd.read_csv(self.users_path)

    def load_items(self):
        return pd.read_csv(self.items_path)

    def add_user(self, user_dict):
        users = self.load_users()

        if 'id' in user_dict and user_dict['id'] is not None:
            new_id = int(user_dict['id'])
        else:
            new_id = int(users['user_id'].max() + 1) if not users.empty else 1

        new_row = {'user_id': new_id, 'name': user_dict.get('name', '')}

        users = pd.concat([users, pd.DataFrame([new_row])], ignore_index=True)
        users.to_csv(self.users_path, index=False)

        return new_id

    def add_item(self, item_dict):
        items = self.load_items()

        if 'id' in item_dict and item_dict['id'] is not None:
            new_id = int(item_dict['id'])
        else:
            new_id = int(items['item_id'].max() + 1) if not items.empty else 1

        new_row = {'item_id': new_id, 'title': item_dict.get('title', '')}

        items = pd.concat([items, pd.DataFrame([new_row])], ignore_index=True)
        items.to_csv(self.items_path, index=False)

        return new_id

    def add_rating(self, user_id, item_id, rating):
        df = self.load_ratings()

        mask = (df['user_id'] == user_id) & (df['item_id'] == item_id)

        if mask.any():
            df.loc[mask, 'rating'] = rating
        else:
            new_row = {'user_id': user_id, 'item_id': item_id, 'rating': rating}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

        df.to_csv(self.ratings_path, index=False)

    def user_exists(self, user_id):
        users = self.load_users()
        return int(user_id) in users['user_id'].values
