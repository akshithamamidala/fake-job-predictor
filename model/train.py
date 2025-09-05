import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.utils import resample
from sklearn.metrics import classification_report
import joblib
import re

# 1️⃣ Load dataset
df = pd.read_csv('fake_job_postings.csv')

# 2️⃣ Basic text cleaning function
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

# 3️⃣ Preprocess text columns
df['description'] = df['description'].apply(clean_text)
df['requirements'] = df['requirements'].apply(clean_text)
df['title'] = df['title'].apply(clean_text)

# 4️⃣ Combine text columns
df['text'] = df['title'] + ' ' + df['description'] + ' ' + df['requirements']

# 5️⃣ Handle missing target column
if 'fraudulent' in df.columns:
    df['target'] = df['fraudulent']
elif 'target' in df.columns:
    df['target'] = df['target']
else:
    raise Exception("No target column named 'fraudulent' or 'target' in dataset.")

# 6️⃣ Split classes
df_majority = df[df.target == 0]
df_minority = df[df.target == 1]

print("Before resampling:")
print(df['target'].value_counts())

# 7️⃣ Downsample majority class
df_majority_downsampled = resample(
    df_majority,
    replace=False,
    n_samples=len(df_minority),
    random_state=42
)

# 8️⃣ Combine balanced dataset
df_balanced = pd.concat([df_majority_downsampled, df_minority])

print("After resampling:")
print(df_balanced['target'].value_counts())

# 9️⃣ Split data
X_train, X_test, y_train, y_test = train_test_split(
    df_balanced['text'],
    df_balanced['target'],
    test_size=0.2,
    random_state=42
)

# 10️⃣ Create pipeline with TF-IDF and Logistic Regression
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(ngram_range=(1,2), max_df=0.9, min_df=3)),
    ('clf', LogisticRegression(max_iter=1000, class_weight='balanced'))
])

# 11️⃣ Train
pipeline.fit(X_train, y_train)

# 12️⃣ Evaluate
y_pred = pipeline.predict(X_test)
print("\nClassification Report on Test Set:")
print(classification_report(y_test, y_pred))

# 13️⃣ Save the model
joblib.dump(pipeline, 'model.joblib')
print("\n✅ Model saved as 'model.joblib'")





