import sys


class WordCount:
    def __init__(self):
        pass

    def main(self):
        all_words_file = open("all_words.txt", "r")
        all_words = all_words_file.read()
        all_words_file.close()
        lines = self.remove_empty_lines(all_words)
        all_words_str = ' '.join(str(line) for line in lines)
        total_words = self.count_words(all_words_str)
        word_count = self.word_count(all_words_str)
        with open("word_counts.txt", "a") as text_file:
            text_file.write('Total Words:' + str(total_words) + '\n')
            text_file.write(str(word_count).encode('utf-8'))
        text_file.close()

    def count_words(self, all_words):
        words = all_words.split(" ")
        num_words = len(words)
        return num_words

    def remove_empty_lines(self, all_words):
        lines = all_words.split("\n")
        for l in lines:
            if not l:
                lines.remove(l)
        return lines

    def word_count(self, all_words):
        counts = dict()
        words = all_words.split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        return counts

wc = WordCount()
wc.main()
