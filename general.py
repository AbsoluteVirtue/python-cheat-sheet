# list all keywords
def list_keywords():
    import keyword
    return keyword.kwlist


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


# download xkcd archive
def xkcd():
    import requests, os, bs4
    url = 'http://xkcd.com'
    os.makedirs('xkcd', exist_ok=True)
    while not url.endswith('#'):
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text)
        comicel = soup.select('#comic img')
        if comicel == []:
            print('Could not find image')
        else:
            comicurl = 'http:' + comicel[0].get('src')
            print('Downloading image {}'.format(comicurl))
            res = requests.get(comicurl)
            res.raise_for_status()
            imgfile = open(os.path.join('xkcd', os.path.basename(comicurl)), 'wb')
            for chunk in res.iter_content(100000):
                imgfile.write(chunk)
            imgfile.close()
        prevlink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevlink.get('href')
    print('Done.')


# Selenium test
def selenium_ex(url, classname, text, email, passw):
    from selenium import webdriver
    browser = webdriver.Firefox()
    browser.get(url)

    try:
        elem = browser.find_element_by_class_name(classname)
        print('found {}'.format(elem.tag_name))
    except:
        print('didn not find element specified')
    linkelem = browser.find_element_by_link_text(text)
    linkelem.click()

    emailelem = browser.find_element_by_id('login-username')
    emailelem.send_keys(email)
    passwordelem = browser.find_element_by_id('login-passwd')
    passwordelem.send_keys(passw)
    passwordelem.submit()


# parse xlsx files
def parse_excel(file):
    import openpyxl
    wb = openpyxl.load_workbook(file)
    sheet = wb.get_sheet_by_name('Sheet1')
    for i in range(1, sheet.max_row + 1):
        print('{} - {}'.format(i, sheet.cell(row=i, column=2).value))


def list_excel_rows(file):
    import openpyxl
    wb = openpyxl.load_workbook(file)
    sheet = wb.get_sheet_by_name('Sheet1')
    for rowObj in sheet['A1':'C3']:
        for cellObj in rowObj:
            print('{} - {}'.format(cellObj.coordinate, cellObj.value))
        print('--- end of row ---')


def list_excel_columns(file):
    import openpyxl
    wb = openpyxl.load_workbook(file)
    sheet = wb.get_sheet_by_name('Sheet1')
    for cellObj in sheet.columns[1]:
        print(cellObj.value)
