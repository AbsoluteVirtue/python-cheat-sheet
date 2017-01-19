def main():
    import general

    # download web page
    page = general.dl_web_page('http://nostarch.com')

    general.parse_html(res=page)

    #

if __name__ == '__main__':
    main()
