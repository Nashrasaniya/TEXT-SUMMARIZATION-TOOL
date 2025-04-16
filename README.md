# TEXT-SUMMARIZATION-TOOL

"Company":CODTECH IT SOLUTIONS

"NAME":MOHAMMED NASHRA SANIYA

"INTERN ID":CODF167

"DOMAIN":ARTIFICIAL INTELLIGENCE MARKUP LANGUAGE

"DURATION:"4 WEEKS

"MENTOR":NEELA SANTHOSH

----> Project Description

This project is a Text Summarization Tool developed as part of Task 1 for the CodTech Internship Program. The primary objective of this tool is to summarize long paragraphs or articles using Natural Language Processing (NLP) techniques. By condensing large text into smaller, meaningful summaries, this tool helps users quickly grasp the main idea without reading through the entire content.

Text summarization is a growing area of NLP that can greatly assist in fields like education, journalism, research, legal documentation, and business reports, where understanding vast amounts of text in limited time is often necessary. This tool is particularly useful for anyone dealing with textual data and in need of automated content summarization without relying on third-party tools or internet access.

The entire project is built using Python, leveraging standard NLP techniques and libraries. The tool runs on the command line and takes a paragraph as input, then returns a concise summary by identifying the most relevant sentences based on frequency analysis.

---> Technologies and Modules Used

This summarizer tool is developed using pure Python and leverages several key libraries and modules:

1. NLTK (Natural Language Toolkit)
Used for tokenizing sentences and words, removing stopwords, and basic NLP processing.

2. String (Python Standard Library)
Utilized for handling punctuation and preprocessing tasks.

3. Heapq (Python Standard Library)
This is used to retrieve the top-ranked sentences based on calculated scores.

These libraries ensure that the solution remains lightweight, efficient, and easily understandable, making it suitable for beginners and intermediate learners in NLP.

---> How It Works – Methodology
The summarization tool follows a clear and logical flow:

1. Input Collection
The user is prompted to paste or enter the full text of a document or article via the terminal.

2. Text Preprocessing

The input is split into sentences and words.

All words are converted to lowercase.

Punctuation and stopwords (like "the", "is", "and") are removed to focus on meaningful content.

3. Word Frequency Calculation

Each non-stopword's frequency is counted and stored.

These frequencies help determine the importance of each word in the context of the entire article.

4. Sentence Scoring

Each sentence is scored based on the sum of word frequencies.

Longer sentences are avoided (typically >30 words) to maintain summary quality.

5. Extracting Top Sentences

The top 3 highest-scoring sentences are selected using the heapq.nlargest() function.

These sentences are combined to form the final summary.

Output
The summary is printed directly to the terminal for user consumption.

--> Features
Simple command-line interface.

1. Lightweight and fast — no need for complex machine learning models.

2. Summarizes any kind of text: articles, essays, blogs, or research notes.

3. Based on proven NLP concepts like tokenization and frequency-based extraction.

--> Real-World Applications
This summarizer tool can be applied in various fields and use cases:

1. News Summarization
Readers can get quick insights into long news articles or press releases.

2. Academic Use
Students and researchers can quickly summarize research papers and journal articles for faster literature reviews.

How to Run
Make sure Python is installed (recommended: Python 3.7+).

1. Install the required packages:

pip install nltk

2. Run the script from your terminal:

3. python summarizer.py

4. Paste your long article or paragraph when prompted.

5. Get your summary in seconds!

---> Conclusion

This project successfully demonstrates how natural language processing techniques can be applied to create practical tools such as text summarizers. It also fulfills the requirements of Task 1 of the CodTech Internship, showing an understanding of core NLP methods like tokenization, stopword removal, and frequency-based scoring.

The tool is easy to use, efficient, and relevant for a wide variety of use cases in both personal and professional contexts.




