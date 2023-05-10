import os
import random
import json
import pandas as pd
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
os.environ["OPENAI_API_KEY"] = "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"

def LLM_chatpgt(training_data, labels):
    all_users = list(training_data.keys())
    llm = OpenAI(temperature=0.9)
    prompt = PromptTemplate(
        input_variables=["user_id","purchase_history"],
        template="Here is the purchase history of {user_id}: {purchase_history} Give a ranked list of 10 items in the order of user preference?",)

    chain = LLMChain(llm=llm, prompt=prompt)
    correct = 0
    for i, user in enumerate(all_users):
        if i % 1 == 0:
            print(f"{i} items for users predicted")
        titles = []
        for item in training_data[user]:
            titles.append(item['title'])
        training_titles = set(titles)
        prediction = chain.run(user_id=user, purchase_history=training_titles)
        df_filtered = labels[labels['reviewerID'] == user]
        label_user = set(df_filtered['title'])
        prediction = prediction.replace("\n", "").replace("\n", "")
        if next(iter(label_user)) in prediction:
            correct += 1

    accuracy = correct / len(labels)
    result = "Amount correct: {} and the HR@10: {}".format(correct, accuracy)
    return result            
