if __name__ == '__main__':
    # with open("main.py") as file:
    #     raw_code = file.read()
    # print(raw_code)

    import pylint.lint

    # pylint_opts = ['--disable=line-too-long', 'main.py']
    # pylint_opts = ['--disable=line-too-long', 'program_file_reading.py']
    pylint_opts = ['--disable=line-too-long', '/home/asif/PycharmProjects/ScrappingScript/Scrapping_Time.py']
    try:
        pylint.lint.Run(pylint_opts)
    except Exception:
        print(Exception)
