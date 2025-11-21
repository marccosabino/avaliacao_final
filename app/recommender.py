import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:
    def __init__(self, storage):
        self.storage = storage
        self.ratings = None
        self.user_item_matrix = None
        self.user_sim = None
        self.user_index = []
        self.item_index = []

    def load_data(self):
        self.ratings = self.storage.load_ratings()
        self.user_item_matrix = self.ratings.pivot_table(
            index='user_id',
            columns='item_id',
            values='rating',
            fill_value=0
        )

        if self.user_item_matrix.shape[0] > 0:
            self.user_sim = cosine_similarity(self.user_item_matrix)
        else:
            self.user_sim = None

        self.user_index = list(self.user_item_matrix.index)
        self.item_index = list(self.user_item_matrix.columns)

    def recommend(self, user_id, n=10):
        if self.user_item_matrix is None or self.user_sim is None:
            self.load_data()

        if user_id not in self.user_index:
            return []

        idx = self.user_index.index(user_id)
        sims = self.user_sim[idx].copy()
        sims[idx] = 0

        ratings_matrix = self.user_item_matrix.values

        numer = sims.dot(ratings_matrix)
        denom = sims.sum()

        scores = numer / (denom + 1e-9) if denom != 0 else numer

        user_ratings = ratings_matrix[idx]
        unrated_mask = user_ratings == 0

        candidate_scores = {
            item: float(scores[i])
            for i, item in enumerate(self.item_index)
            if unrated_mask[i]
        }

        top_items = sorted(candidate_scores.items(), key=lambda x: x[1], reverse=True)[:n]

        items_df = self.storage.load_items()
        id_to_title = dict(zip(items_df['item_id'], items_df['title']))

        return [
            {
                'item_id': int(item_id),
                'score': float(score),
                'title': id_to_title.get(item_id, str(item_id))
            }
            for item_id, score in top_items
        ]
