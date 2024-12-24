This code is a Python program designed to perform several tasks related to keyword tracking, web crawling for related content, and filtering words. Here’s an overview of what the program does:

1. **File Input/Output Functionality**:
    - **`load_keywords_with_counts(file_path)`**: This function loads previously saved keywords and their counts from a file.
    - **`save_keywords_with_counts(file_path, keywords)`**: This function saves the keywords and their counts to a file.
    - **`increment_keyword_count(keywords, keyword)`**: This function increments the count of a given keyword in the keywords dictionary.
2. **Web Crawling Functionality**:
    - **`crawl_related_keywords_and_sentences(keyword)`**: This function crawls Google search results for the specified keyword. It extracts related keywords and sentences containing the input keyword from the first two pages of search results. It also filters out irrelevant and unwanted content.
3. **Keyword Filtering Functionality**:
    - **`filter_words_with_keyword(words, keyword)`**: This function filters and returns words that contain the specified keyword from a given set of words.
4. **Main Program**:
    - The main program performs the following steps:
        - Loads previously entered keywords and their counts from a file.
        - Continuously prompts the user to enter a keyword until the user types 'quit'.
        - Increments the count for each entered keyword.
        - Crawls the web to find related keywords and sentences containing the entered keyword.
        - Displays related keywords and sentences to the user.
        - Extracts and filters words containing the entered keyword from the collected sentences.
        - Displays the filtered words to the user.
        - Saves the updated keywords and their counts back to the file.

Additionally, the program prioritizes displaying the keyword if it has been entered five or more times.

### **Main Flow of the Program:**

1. Load existing keywords and counts from a file.
2. Prompt the user to enter a keyword.
3. Increment and update the count for the entered keyword.
4. Use web crawling to fetch related keywords and sentences from Google search results.
5. Extract and filter words containing the entered keyword.
6. Display the related keywords, sentences, and filtered words.
7. Save the updated keywords and counts to the file.

This program is useful for tracking keyword usage, discovering related keywords, and extracting contextual information from web search results.
