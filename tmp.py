import os

# print(os.listdir('../ocr_crnn_001/test.txt'))

file = open("../ocr_crnn_001/train.txt")

for i in range(0, 3000):
    line = file.readline()
    path = '../ocr_crnn_001/images/'+line.replace('\n', '').split(' ')[0]
    newPath = '../ocr_crnn_001/tmp'
    if os.path.exists(path):
        commond = 'cp ' + path + ' ' + newPath
        os.system(commond)
    else:
        print(path)
