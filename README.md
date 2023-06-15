Test(s) of openai's gpt api.

The main one here for now is a proof of concept ocr correction.
jp_text_words.txt contains the raw text from an ocr scan of a list of english word frequencies of textbooks used in highschools in Japan.

In text_correction.py, it is sent 50 lines at a time to extract the english words and fix scanning error.

output.txt is the output of text_correction.py. 

The current prompt does not provide 100% consistent formatting on output. But it is now in a format that can be solved with minimal editing vs the original ocr scan.

text_match.py is a potential usecase of this new list of words, taking an example essay, and returning a list of words that do not appear in the textbook list. This can be used to inform future lesson plans, to better cover vocabulary, or to provide exams using words that students have more likely encountered before.