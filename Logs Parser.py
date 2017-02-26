import os

songlist = []
cwd = os.getcwd()
name_of_file = str(input("Enter the name of the file you want to parse from. NOTE: YOUR INPUT MUST END IN .txt "))
new_name_of_file = str(input("Enter the name of the file you want as your output. NOTE: YOUR INPUT MUST END IN .txt" ))

'''
Will this program work for filetypes other than .txt?'''

def getfromlogs(filename=os.path.join(cwd, name_of_file)):
    global songlist
    with open(filename, 'r', encoding='utf-8') as f:
        f.seek(0)
        while True:
            data = f.readline()
            if '!play' in data:
                songlist.append(data)
            if data == '':
                break
    return songlist

def exportfromlogs(list=songlist,xfile=os.path.join(cwd, new_name_of_file)):
    with open(xfile, 'w') as fp:
        for each_song in songlist:
            try:
                fp.write(each_song)
            except:
                pass
            
if __name__ == '__main__':
    print("Hang on, program is running...")
    getfromlogs()
    exportfromlogs()
