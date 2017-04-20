from __future__ import print_function

import json
import urllib2

# print('Loading function')


def main():
    url = 'https://api.nytimes.com/svc/books/v3/lists.json?api-key=4c6992402d6a4f9fa7eb5b95f1f69d03&list=%s'
    fields = ['title', 'author']
    sections = ['hardcover-nonfiction']#, 'combined-print-and-e-book-nonfiction']
    new_bests = {}
    for section in sections:
        new_bests[section] = {}
        books_url = url % (section)
        ## limit to top 15 books as only they have weeks_on_list field
        # content = requests.get(books_url, timeout=60).json()#['results'][:15]
        content = urllib2.urlopen(books_url).read()#, timeout=60)
        # return content
        data = json.loads(content)
        data = data['results'][:15]
        # if book recent addition to best seller list add to new_bests dict
        for book in data:
        # if a book has been on list 15 weeks or less
            if book['weeks_on_list']:# <= 15:
                book_details = book['book_details'][0]
                title = book_details['title']
                new_bests[section][title] = \
                    (book_details['author'], book['weeks_on_list'])
    books = {}
    i = 0
    text_body = ''
    ## loop through sections and get unique books for each
    for section in sections:
        for (title, author_weeks) in new_bests[section].items():
            if title in books:
                continue
            else:
                # first line print header
                if i == 0:
                    text_body +=\
                    '\n\tNew books on New York Times best sellers list (non-fiction): \n\n\t\t- %s by %s\n'\
                        % (title, author_weeks[0])
                    i = 1
                else: 
                    text_body += '\t\t- %s by %s\n' % \
                            (title, author_weeks[0])
                books[title] = author_weeks[0]
    print(text_body)
    # return ''.join(list(books.items()))

if __name__ == '__main__':
    main()