import collections


def parse_user_data(line):
    """
    >>> parse_user_data('John Doe john.doe@example.com')
    ('John', 'Doe', 'john.doe', 'example.com')
    """
    first_name, last_name, user, host = line.replace('@', ' ').split(' ')
    response = (first_name, last_name, user, host)
    return response


def compare_lists(dir_a, dir_b):
    """
    >>> dir_a = ['hello.py', 'readme.txt']
    >>> dir_b = ['readme.txt', 'install.txt', 'hello2.py']
    >>> compare_lists(dir_a, dir_b)
    {'removed': ['hello.py'], 'added': ['hello2.py', 'install.txt']}
    """

    removed = [filename for filename in dir_a if filename not in dir_b]
    added = [filename for filename in dir_b if filename not in dir_a]
    return {'removed': sorted(removed), 'added': sorted(added)}


def print_log(message, process_id, timestamp, level=2):
    """
    >>> from datetime import datetime
    >>> print_log('System started!', 1532, datetime(2019, 1, 2, 10, 30, 55).isoformat(' '))
    2019-01-02 10:30:55 [1532] [INFO] System started!
    """
    loglevel = {0: 'TRACE', 1: 'DEBUG', 2: 'INFO', 3: 'WARN', 4: 'ERROR'}.get(level)
    print(f'{timestamp} [{str(process_id)}] [{loglevel}] {message}')


def biggest_rectangle(rectangles):
    """
    Find the biggest rectangle in a sequence.
    Rectangles are represented as tuples of (width, height).

    >>> biggest_rectangle([(2, 4), (3, 3), (4, 2)])
    (3, 3)
    """
    return [side for side in rectangles if side[0]*side[1] == max([side[0]*side[1] for side in rectangles])][0]

    # rectangles.sort(key=max)
    # return rectangles[0]


def find_in_file(pattern, filename):
    """
    Find a pattern in file. Print out all lines that match the pattern
    (case-insensitive) with line numbers.

    >>> find_in_file('nevermore', 'raven.txt')
     62 Quoth the Raven, "Nevermore."
     69 With such name as "Nevermore."
     77 Then the bird said, "Nevermore."
     84 Of 'Never- nevermore'."
     92 Meant in croaking "Nevermore."
     99 She shall press, ah, nevermore!
    107 Quoth the Raven, "Nevermore."
    115 Quoth the Raven, "Nevermore."
    123 Quoth the Raven, "Nevermore."
    132 Quoth the Raven, "Nevermore."
    140 Shall be lifted- nevermore!
    """
    with open(filename) as file:
        lines = file.readlines()
        solution = list(enumerate([line.strip() for line in lines]))
        print('\n'.join([' '.join((str(line[0]).rjust(3), line[1])) for line in solution if pattern.lower() in line[1].lower()]))


def read_long_words(filename, min_length=0):
    """
    >>> words = read_long_words('raven.txt', 5)
    >>> words[:6]
    ['midnight', 'dreary', 'pondered', 'quaint', 'curious', 'volume']
    """
    with open(filename) as file:
        text = file.read()
        return [word.strip('\n.,"!-').lower() for word in text.split(' ') if len(word.strip('\n.,"!-')) > min_length]


def top_words(words, n=10):
    """
    Find top N words in a file. Return a list of tuples (word, count).

    >>> words = read_long_words('raven.txt', 5)
    >>> top_words(words, 5)
    [('chamber', 11), ('nevermore', 10), ('lenore', 8), ('nothing', 7), ('tapping', 5)]
    """

    words = sorted([(word, collections.Counter(words)[word]) for word in set(words)], key=lambda x: x[1], reverse=True)
    return words[:n]
