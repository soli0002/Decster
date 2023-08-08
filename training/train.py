import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib


print('Loading data from CSV...')
# Load data from the CSV file
data = pd.read_csv('training_data.csv')


print('Separating features...')
# Separate features (X) and labels (y)
X = data['Encoded Text']
y = data['Encoding Type']


print('Splitting data into training/testing...')
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


print('Creating vectorizer...')
# Create the TF-IDF vectorizer
vectorizer = TfidfVectorizer()


print('Converting text to TF-IDF...')
# Convert text data to numerical TF-IDF features
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)


print('Creating model...')
# Create the model
model = SVC(kernel='linear')


print('Training...')
# Train the model on the training data
model.fit(X_train_tfidf, y_train)

# Predict on the testing data
y_pred = model.predict(X_test_tfidf)

print('Evaluating...')
# Evaluate the model on the testing data
accuracy = model.score(X_test_tfidf, y_test)
print("Model accuracy:", accuracy)

print('Saving model to file...')
joblib.dump(model, 'trained_model.pkl')

print('Done!')