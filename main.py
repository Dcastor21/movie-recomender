import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

# fetch data and format it
print(repr(data['train']))
print(repr(data['test']))

# create Model
model = LightFM(loss='warp')
# train model
model.fit(data['train'], epochs=30, num_threads=2)

def sample_recommendation(model, data, user_id):

  # number of users and movies in training data
  n_users, n_items = data['train'].shape

  # generate recommendations for each user we input
  for user_id in user _ids:
  # movies they already like
    known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]
    # movies they have not seen yet
    scores = model.predict(user_id, np.arange(n_items))
    # rank the movies in order of their predicted score
    top_items = data['item_labels'][np.argsort(-scores)]

    # print out the resutl
    print("User %s" % user_id)
    print("     Known positives:")

    for x in known_positives[:3]:
      print("         %s" % x)

    print("     Recommended:")
    for x in top_items[:3]:
      print("         %s" % x)

sample_recommendation(model, data,[10,16,250])