class CaseStudy:
    def __init__(self, title, publish_year, language, price):
        self.title = title
        self.publish_year = publish_year
        self.language = language
        self.price = price


class Book(CaseStudy):
    def __init__(self, title, publish_year, language_book, price, author, pages, progress=None):
        self.author = author
        self.pages = pages
        self.left_pages = pages
        self.update_pages = pages
        self.progress = progress
        super().__init__(title, publish_year, language_book, price)

    def read(self, page):
        self.left_pages = self.pages - page
        self.update_pages = self.pages - self.left_pages
        self.progress = round((page / self.pages) * 100)
        return f"Progress is {self.progress}%"

    def get_status(self, page):
        self.left_pages = self.pages - page
        if self.left_pages == self.pages:
            return "no pages has been read yet"
        elif 0 < self.left_pages < self.pages:
            return "reading the book"
        elif self.left_pages == 0:
            return "all pages has been read"

    def __str__(self):
        return f"Book) \nTitle:{self.title} \nauthor(s):{self.author} \nPublish_year:{self.publish_year}" \
               f" \nPages(number of pages):{self.pages} \nLanguage:{self.language} \nPrice:{self.price} "


class Magazine(Book):
    def __init__(self, title, publish_year, language, price, author, pages, issue):
        self.issue = issue
        super().__init__(title, publish_year, language, price, author, pages)

    def __str__(self):
        return f"Magazine) \nTitle:{self.title} \nAuthor(s):{self.author} \nPublish year:{self.publish_year} " \
               f"\nLanguage:{self.language} \nPrice:{self.price}  \nIssue:{self.issue} "


class PodcastEpisode(CaseStudy):
    def __init__(self, title, publish_year, language, price, speaker, time, progress=None):
        self.speaker = speaker
        self.time = time
        self.left_time = time
        self.update_time = time
        self.progress = progress
        super().__init__(title, publish_year, language, price)

    def listen(self, time_):
        self.left_time = self.time - time_
        self.update_time = self.time - self.left_time
        self.progress = round((time_ / self.time) * 100, 2)
        return f"Progress is {self.progress}%"

    def get_status(self, time_):
        self.left_time = self.time - time_
        if self.left_time == self.time:
            return "no times has been read yet"
        elif 0 < self.left_time < self.time:
            return "listening the podcast"
        else:
            return "all times has been listen)"

    def __str__(self):
        return f"Podcast) \nTitle:{self.title} \nSpeaker:{self.speaker} \npublish-year:{self.publish_year}" \
               f"\ntime:{self.time} \nLanguage:{self.language} \nPrice:{self.price}"


class Audiobook(PodcastEpisode):
    def __init__(self, title, publish_year, language, price, speaker, time, author, pages, audio_language):
        self.author = author
        self.pages = pages
        self.audio_language = audio_language
        super().__init__(title, publish_year, language, price, speaker, time)

    def __str__(self):
        return f"Adiobook)\nTitle:{self.title} \nSpeaker:{self.speaker} \nauthor:{self.author} " \
               f"\nPulish-year:{self.publish_year}  \nPages:{self.pages}  \ntime:{self.time}" \
               f"\nbook_Language:{self.language} \naudio_language:{self.audio_language} \nPrice:{self.price} "


list_case_study = []
book = []
magazine = []
podcast_episode = []
audiobook = []
book_list = []
import sys


##########################Create mediatype####################################

def get_data(media_type):
    ###################Mediatype: Book######################
    if media_type == "Book":
        title_book = input("Please enter a book title: ")
        author_book = input("Please enter author(s): ")
        publish_year_book = input("Please enter year of publish: ")
        pages_book = int(input("Please enter pages of book: "))
        language_book = input("Please enter language of book: ")
        price_book = input("Please enter a price book: ")
        page_ = int(input("Please enter pages read: "))
        book = Book(title_book, publish_year_book, language_book, price_book, author_book, pages_book)
        list_case_study.append(book)


        print("###############Book###################")
        print(book)
        print(book.get_status(page_))
        print(book.read(page_))
        print('\n')
    ###################Mediatype: Magazine######################
    elif media_type == "Magazine":
        title_magazine = input("Please enter a magazine title: ")
        author_magazine = input("Please enter author(s): ")
        publish_year_magazine = input("Please enter year of publish: ")
        pages_magazine = int(input("Please enter pages of magazine: "))
        language_magazine = input("Please enter language of magazine: ")
        price_magazine = input("Please enter a magazine price: ")
        issue_magazine = input("Please enter the issue: ")
        page_ = int(input("Please enter pages read: "))
        magazine = Magazine(title_magazine, publish_year_magazine,
                            language_magazine, price_magazine, author_magazine, pages_magazine, issue_magazine)
        list_case_study.append(magazine)

        print("###############Magazine###################")
        print(magazine)
        print(magazine.get_status(page_))
        print(magazine.read(page_))
        print('\n')

    ###################Mediatype: Podcast######################
    elif media_type == "Podcast":
        title_podcast_episode = input("Please enter a podcast episode title: ")
        publish_year_podcast_episode = input("Please enter year of publish: ")
        language_podcast_episode = input("Please enter language of podcast episode: ")
        price_podcast_episode = input("Please enter a podcast episode price: ")
        speaker_podcast_episode = input("Please enter speaker: ")
        time_podcast_episode = int(input("Please enter time of podcast episode: "))
        time_ = int(input("Please enter time listen: "))
        podcast_episode = PodcastEpisode(title_podcast_episode, publish_year_podcast_episode, language_podcast_episode
                                         , price_podcast_episode, speaker_podcast_episode, time_podcast_episode)
        list_case_study.append(podcast_episode)

        print("###################Podcast#######################")
        print(podcast_episode)
        print(podcast_episode.get_status(time_))
        print(podcast_episode.listen(time_))
        print('\n')

    ###################Mediatype: Audiobook######################
    elif media_type == "Audiobook":
        title_audiobook = input("Please enter a Audiobook title: ")
        publish_year_audiobook = input("Please enter year of publish: ")
        language_audiobook = input("Please enter language of Audiobook: ")
        price_audiobook = input("Please enter a Audiobook price: ")
        speaker_audiobook = input("Please enter speaker: ")
        time_audiobook = int(input("Please enter time of Audiobook: "))
        author_audiobook = input("Please enter author(s): ")
        pages_audiobook = input("Please enter pages of Audiobook: ")
        audio_language_audiobook = input("Please enter audio_language of Audiobook: ")
        time_ = int(input("Please enter time read: "))
        audiobook = Audiobook(title_audiobook, publish_year_audiobook, language_audiobook, price_audiobook,
                              speaker_audiobook, time_audiobook, author_audiobook, pages_audiobook,
                              audio_language_audiobook)
        list_case_study.append(audiobook)
        print("###################Audiobook######################")
        print(audiobook)
        print(audiobook.get_status(time_))
        print(audiobook.listen(time_))


media_type_ = []
I = int(input("Enter number of case study:"))
for i in range(1, I + 1):
    media_type = input("pleas enter a media type :")
    media_type_.append(media_type)
    get_data(media_type)
    bookshelf_list = sorted(list_case_study, key=lambda x:
    x.progress, reverse=True)
    for _ in bookshelf_list:
       print('{',_.title,_.progress,'}')

    out = input("Enter 0 if you want to stop the program: ")
sys.exit(out)
