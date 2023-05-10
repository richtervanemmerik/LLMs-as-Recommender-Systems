def global_popularity_based_method(data, labels, top_n):
    correct = 0
    popularity_df = data.groupby('title').size().reset_index(name='popularity_score')
    global_recommended_items = recommend_items(popularity_df, top_n)
    for title in labels['title']:
        if title in global_recommended_items:
            correct += 1
    accuracy = correct / len(labels)
    result = "Amount correct: {} and the HR@10: {}".format(correct, accuracy)
    return result
def recommend_items(popularity_df, top_n):
    popularity_rank = popularity_df.sort_values(by='popularity_score', ascending=False)
    recommended_items = popularity_rank.head(top_n)['title'].values
    global_recommended_items = ", ".join(recommended_items)
    return global_recommended_items            