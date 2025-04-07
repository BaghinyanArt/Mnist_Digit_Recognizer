import zipfile
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB, GaussianNB, MultinomialNB
from sklearn.metrics import accuracy_score, f1_score, recall_score

path = r'C:\Users\Artur\Downloads\sms+spam+collection.zip'
with zipfile.ZipFile(path, 'r') as zip_ref:
    zip_ref.printdir()
    name = 'SMSSpamCollection'
    with zip_ref.open(name) as file:
        df = pd.read_csv(file, sep='\t', header=None, names=['label', 'message'])

messages = df['message']
tfidf_vectorizer = TfidfVectorizer()
X_tfidf = tfidf_vectorizer.fit_transform(messages)
tfidf_dtm = pd.DataFrame(X_tfidf.toarray(), columns=tfidf_vectorizer.get_feature_names_out())
df_new = pd.concat([df['label'], tfidf_dtm], axis=1)
df_new['label'] = df_new['label'].map({'ham': 0, 'spam': 1})

X = df_new.drop('label', axis=1) 
y = df_new['label'] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
bnb_model = BernoulliNB()
bnb_model.fit(X_train, y_train)
y_pred = bnb_model.predict(X_test)

print("Bernoulli Naive Bayes Performance:")
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.4f}")
print(f"F1-score: {f1:.4f}")
print(f"Recall  : {recall:.4f}")
