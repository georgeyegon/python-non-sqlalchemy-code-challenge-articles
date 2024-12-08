class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and (5 <= len(new_title) <= 50):
            self._title = new_title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine

class Author:
    def __init__(self, name):
        self.name = name
        self.articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance (new_name, str) and len(new_name) > 0 and not hasattr(self, "name"):
            self._name = new_name

    def articles(self):
        return [article for article in Article.all if article.author is self]

    def magazines(self):
        return list(set([article.magazine for article in Article.all if article.author is self]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self): 
        first_list = [article.magazine for article in Article.all if article.author is self]
        if len(first_list) > 0:
            return list(set([magazine.category for magazine in first_list]))
        else:
            return None
        pass

class Magazine:
    all_m = []  

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
        Magazine.all_m.append(self)

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category
    
    @name.setter 
    def name(self, _name):
        if isinstance(_name, str) and 2 <= len(_name) <= 16:
            self._name = _name

    @category.setter 
    def category(self, _category):
        if isinstance(_category, str) and len(_category) > 0:
            self._category = _category

    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list(set([article.author for article in Article.all if article.magazine is self]))

    def article_titles(self):
        list_titles = [article.title for article in Article.all if article.magazine is self]
        if len(list_titles) > 0:
            return list_titles
        else:
            return None

    def contributing_authors(self):
        all_cont = [article.author for article in Article.all if article.magazine is self]
        for element in all_cont:
            if all_cont.count(element) >= 2:
                return [element for element in all_cont]
            else: 
                return None

    def add_article(self, author, title):
        article = Article(author, self, title)
        self._articles.append(article)  
        return article

    @classmethod
    def top_publisher(cls):
        if not cls.all_m:
            return None
        return max(cls.all_m, key = lambda magazine: len(magazine.articles()))

magazine1 = Magazine("The New Yorker", "Politics")

author1 = Author("John Doe")