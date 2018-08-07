import dataset
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

def calculate_all_distances(title):
    
    data = dataset.execute()
    
    def cosine_sim(text1, text2):
        #vectorizer = CountVectorizer(strip_accents='unicode', decode_error='ignore', analyzer='word', ngram_range=(1,1), stop_words='english')
        vectorizer = TfidfVectorizer(stop_words='english')
        matrice = vectorizer.fit_transform([text1, text2])
        return ((matrice * matrice.T).A)[0,1]
    
    results = []
    text_X = None
    for sample in data:
        print(sample['title'])
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
    print(recipes[:num])  

if __name__ == '__main__':
    
    recipes = calculate_all_distances('Artichoke and Parmesan Risotto')
    display_similar_recipes(10, recipes)