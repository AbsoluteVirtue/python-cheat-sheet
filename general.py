# list all keywords
def list_keywords():
    import keyword
    keyword.kwlist


# show variable's unique identity
def show_var_id(var):
    id(var)


# show object's type
def show_obj_type(var):
    type(var)


# list all standard types
def list_standard_types():
    import types
    dir(types)


# calculate factorial of N
def factorial(n):
    assert n > 0
    if n != 0:
        return n * factorial(n-1)
    else:
        return 1


# list all attributes in a module
def list_all_module():
    import copy
    return [name for name in dir(copy) if name[0] != '_']


# use iterator constructor to iterate over a list
def iter_constructor():
    iter_list = [1, 2, 3]
    iterator = iter(iter_list)
    print(list(iterator))


# example of a generator
def generator_ex(low, high):
    for a in range(low, high):
        yield a
    for b in range(high-2, low-1, -1):
        yield b


# example of a class
class Range(object):
    def __init__(self, start=0, end=10):
        self.counter = start
        self.end = end

    def next(self):
        if self.counter < self.end:
            res = self.counter
            self.counter += 1
            return res
        else:
            return None


# display Zen of Python
def zen():
    import this


# calculate square root using Newton's method
def square_root(a, estimated):
    epsilon = 0.0000001
    while True:
        print(estimated)
        result = (estimated + a / estimated) / 2
        if result == estimated:
            break
        elif abs(result - estimated) < epsilon:
            break
        estimated = result


# find all occurrences of emails in a text block from clipboard
def find_all_emails(regex):
    import pyperclip

    text = str(pyperclip.paste())
    matches = []
    for groups in regex.findall(text):
        matches.append(groups[0])

    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copied:')
        print('\n'.join(matches))
    else:
        print('Nothing found.')


# copy files, returns a path to the newly copied file
def copy_file(source, destination):
    import shutil, os
    os.chdir('C:\\')
    return shutil.copy(source, destination)


# list files and write them to a text file
def list_files(path, extension):
    import zipfile, os
    for folder, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.{}'.format(extension)):
                print("FOLDER: {}".format(folder))
                print(filename)
                with open("test.txt", 'a', encoding='utf-8') as log:
                    log.write(folder + '\n')
                    log.write(u"{}\n".format(filename))
            # elif filename.endswith('.zip'):
                # with zipfile.ZipFile(filename) as archive:
                    # print(archive.namelist())


# open a web-browser
def web_browser(url):
    import webbrowser
    webbrowser.open(url)


# download a web page
def dl_web_page(url):
    import requests
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem handling your request: {}'.format(exc))
    print('Status code: {}'.format(res.status_code))
    print(res.text[:250])
    return res


# write the web page to a text file
def write_web_to_txt(res):
    dl_file = open('web.txt', 'wb')
    for chunk in res.iter_content(100000):
        dl_file.write(chunk)
    dl_file.close()


# parse html
def parse_html(res=None, filename=''):
    import bs4
    if res is None and filename == '':
        return
    elif res is None and filename != '':
        file = open(filename)
        soup = bs4.BeautifulSoup(file, "lxml")
        print(soup.text[:250])
    else:
        try:
            res.raise_for_status()
        except Exception as exc:
            print('There was a problem handling your request: {}'.format(exc))
        print('Status code: {}'.format(res.status_code))
        soup = bs4.BeautifulSoup(res.text, "lxml")
        print(soup.text[:250])
