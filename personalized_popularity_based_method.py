def personalized_popularity_based_method(data, labels, top_n):
    correct = 0
    for index, (user_id, title) in enumerate(labels[['reviewerID', 'title']].values):
        if index % 10 == 0:
            print(f"{index} items for users predicited")    
        recommended_items = recommend_items(data, user_id, top_n)
        personlized_recommended_items = ", ".join(recommended_items)
        if title in personlized_recommended_items:
            correct += 1
    accuracy = correct / len(labels)

    result = "Amount correct: {} and the HR@10: {}".format(correct, accuracy)
    return result




def recommend_items(data, user_id, top_n):
    popularity_df = data.groupby(['reviewerID', 'title']).size().reset_index(name='popularity_score')
    user_products = data[data['reviewerID'] == user_id]['title']
    user_unseen_products = data[~data['title'].isin(user_products)]['title']
    user_popularity = popularity_df[(popularity_df['title'].isin(user_unseen_products))]
    user_popularity = user_popularity.sort_values(by='popularity_score', ascending=False)
    return user_popularity.head(top_n)['title'].values    
