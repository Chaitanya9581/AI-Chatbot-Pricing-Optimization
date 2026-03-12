import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

responses = {
    "hello": "Hello! How can I help you today?",
    "price": "Our pricing is dynamically optimized based on demand.",
    "product": "We offer high-quality AI-powered products.",
    "bye": "Goodbye! Have a great day!"
}

questions = list(responses.keys())
answers = list(responses.values())

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

def chatbot_response(user_input):
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)
    index = similarity.argmax()

    if similarity[0][index] > 0.3:
        return answers[index]
    else:
        return "Sorry, I didn't understand that. Please ask something else."
