import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

def summarize_text(text, num_sentences=5):
    # Tokenize sentences and words
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())

    # Filter stopwords and non-alphanumeric words
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

    # Frequency distribution
    freq_dist = FreqDist(filtered_words)

    # Score sentences based on word frequency
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in freq_dist:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq_dist[word]

    # Sort sentences by score and return the top ones
    sorted_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    summary = ' '.join(sorted_sentences[:num_sentences])
    return summary


if __name__ == "__main__":
    print("----- Text Summarizer Tool (Task 1 - CodTech Internship) -----")
    input_text = input("Paste your article or paragraph:\n\n")

    if input_text.strip() == "":
        print("\n Error: No input text provided.")
    else:
        summary = summarize_text(input_text)
        print("\n----- Summary Output -----\n")
        print(summary)
