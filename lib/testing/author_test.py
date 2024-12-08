class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []  # Use a private variable to store the articles

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def articles(self):
        return self._articles
