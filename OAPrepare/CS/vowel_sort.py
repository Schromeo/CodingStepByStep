'''
给定一个字符串 text，它由被空格分隔的、唯一的、小写的英语单词组成。 
你的任务是计算每个单词中元音（'a', 'e', 'i', 'o', 'u'）和辅音的数量，并算出它们之间数量的绝对差值。 
你需要返回一个按这个绝对差值升序排列的单词数组。如果两个单词的绝对差值相同，则按字母顺序对这两个单词进行排序。

Example 1:

For text = "penelope lives in hawaii", the output should be solution(text) = ["in", "penelope", "lives", "hawaii"].

Explanation:

"penelope": 4 vowels, 4 consonants. Diff = 0.

"lives": 2 vowels, 3 consonants. Diff = 1.

"in": 1 vowel, 1 consonant. Diff = 0.

"hawaii": 4 vowels, 2 consonants. Diff = 2.

Sorting by diff: 0, 0, 1, 2.

The two 0-diff words ("penelope", "in") are sorted alphabetically: "in" comes before "penelope".

Final order: "in", "penelope", "lives", "hawaii"
'''
def solution(text):
    w = text.split()
    l = []
    vs = set('aeiou')
    for word in w:
        v = sum(1 for c in word if c in vs)
        c = len(word) - v
        d = abs(c - v)
        l.append((d, word))
    l.sort()
    return [x[1] for x in l]