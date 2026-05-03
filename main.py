import re

#створюємо клас літер
class Letter:
    def __init__(self, char):
        self.char = char

    def __str__(self):
        return self.char


#створюємо клас слів
class Word:
    def __init__(self, word_string):
        self.letters = [Letter(c) for c in word_string]

    def get_length(self):
        return len(self.letters)

    def __str__(self):
        return "".join(str(l) for l in self.letters)

    def __eq__(self, other):
        if not isinstance(other, Word):
            return False
        return str(self) == str(other)


#створюмо клас розділових знаків
class Punctuation:
    def __init__(self, char):
        self.char = char

    def __str__(self):
        return self.char


#створюємо клас речень
class Sentence:
    def __init__(self, sentence_string):
        self.elements = []
        clean_s = " ".join(sentence_string.split())
        tokens = re.findall(r"[\w']+|[.,!?;:-]", clean_s)
        for token in tokens:
            if re.match(r"[.,!?;:-]", token):
                self.elements.append(Punctuation(token))
            else:
                self.elements.append(Word(token))

#рахує слова
    def get_word_count(self):
        return sum(1 for e in self.elements if isinstance(e, Word))

#формує "читабельний" вигляд
    def __str__(self):
        result = []
        for i, elem in enumerate(self.elements):
            s_elem = str(elem)
            if i > 0 and isinstance(elem, Word) and not isinstance(self.elements[i-1], Punctuation):
                result.append(" " + s_elem)
            else:
                result.append(s_elem)
        return "".join(result)

#шукає задане речення
    def __eq__(self, other):
        if not isinstance(other, Sentence):
            return False
        return str(self) == str(other)


#виконавчий метод
class MainExecutor:
    @staticmethod
    def run():
#створює масив з 5 об'єктів
        sentences = [
            Sentence("Сьогодні рано зійшло сонце."),
            Sentence("Воно гріє і від цього стає затишно, тепло на душі."),
            Sentence("Відчуваю енергію сонця."),
            Sentence("Дивлюсь у вікно і всі люди також радісні, безтурботні, наче все вже у минулому."),
            Sentence("Почались перші дні тепла.")
        ]

        print("Початковий список речень")
        for s in sentences:
            print(f"[{s.get_word_count()} слів] {s}")

#сортування за кількістю слів (зростання) і сортування за довжиною першого слова в реченні (спадання)
        sentences.sort(key=lambda s: (s.get_word_count(), -len(str(s.elements[0]))))

        print("\nВідсортований масив")
        for s in sentences:
            print(s)

#шукає задане нами речення
        target = Sentence("Воно гріє і від цього стає затишно, тепло на душі.")
        found = next((s for s in sentences if s == target), None)

        print("\nРезультат пошуку")
        if found:
            print(f"Знайдено ідентичне речення: {found}")
        else:
            print("Не знайдено.")


if __name__ == "__main__":
    MainExecutor.run()
