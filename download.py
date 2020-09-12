def download(links, overwrite = False, save_to="."):
    for file in links:
        filename = urllib.parse.unquote(os.path.basename(file))
        filepath = save_to+"/"+filename
        fileexist = os.path.isfile(filepath)
        if (fileexist):
            print(filename+" is already existed.")
        if (overwrite):
            print('Downloading (overwrite) '+filename)
            tst = urllib.request.urlretrieve(file, savetofile)
        else:
            print("Skip downloading "+filename)
            continue
