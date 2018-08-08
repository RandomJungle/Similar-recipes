import dataset
import tkinter
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from time import sleep

DATA = dataset.execute()
TITLES = [sample['title'] for sample in DATA]

def calculate_all_distances(title, data):
    
    def cosine_sim(text1, text2):
        #vectorizer = CountVectorizer(strip_accents='unicode', decode_error='ignore', analyzer='word', ngram_range=(1,1), stop_words='english')
        vectorizer = TfidfVectorizer(stop_words='english')
        matrice = vectorizer.fit_transform([text1, text2])
        return ((matrice * matrice.T).A)[0,1]
    
    results = []
    text_X = None
    for sample in data:
        # extract text of selected recipe
        if sample['title'] == title :
            text_X = ' '.join(sample['directions'])
    for sample in data :
        if sample['title'] != title :
            text_Y = ' '.join(sample['directions'])
            # Compute distance with X
            if text_X is not None :
                similarity = cosine_sim(text_X, text_Y)
                results.append((sample['title'], similarity))
    return results

def display_similar_recipes(num, recipes):
    
    recipes.sort(key=lambda tup: tup[1], reverse=True)
    for i in range(0,num+1):
        print(recipes[i])
        print('\n')
        
def execute():
    
    title = 'Turkey Cream Puff Pie'
    results = calculate_all_distances(title, DATA)
    display_similar_recipes(10, results)

if __name__ == '__main__':
    
    execute()