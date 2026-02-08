def analyze_text():
    print("--- 📝 Text Analyzer ---")
    text = input("Enter a sentence or paragraph: ")
    
    # Logic
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    avg_word_length = char_count / word_count if word_count > 0 else 0
    
    print(f"\nAnalysis Results:")
    print(f"- Total Words: {word_count}")
    print(f"- Total Characters (with spaces): {char_count}")
    print(f"- Average Word Length: {avg_word_length:.2f}")

analyze_text()
