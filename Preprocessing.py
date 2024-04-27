import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')

# Function for tokenization
def tokenize(text):
    tokens = nltk.word_tokenize(text.lower())
    return tokens[:500]

# Function for stop-word removal
def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    return filtered_tokens

# Function for stemming
def stem_tokens(tokens):
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return stemmed_tokens

# Read the CSV file
# data = pd.read_csv('TravelData.csv')
# data = pd.read_csv('HealthAndFitnessData.csv')
data = pd.read_csv('Data Scrapping/ScienceAndEducationData.csv')

# Preprocess text data
preprocessed_texts = []
for text in data['Paragraph']:
    tokens = tokenize(text)
    tokens = remove_stopwords(tokens)
    stemmed_tokens = stem_tokens(tokens)
    preprocessed_text = ' '.join(stemmed_tokens)
    print("*********************************************")
    print(preprocessed_text)
    preprocessed_texts.append(preprocessed_text)

# Update the DataFrame with preprocessed text
data['preprocessed_text'] = preprocessed_texts

# Save the preprocessed data to a new CSV file
# data.to_csv('preprocessed_travel_data.csv', index=False)
# data.to_csv('preprocessed_health_and_fitness_data.csv', index=False)
data.to_csv('preprocessed_science_and_education_data.csv', index=False)