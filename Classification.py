from os.path import exists
import shutil

for x in range(1440):
    if exists(f'../CNN/BurnsDataSet/img{x}.txt' and f'../CNN/BurnsDataSet/img{x}.jpg'):
        with open(f'../CNN/BurnsDataSet/img{x}.txt') as f:
            label = f.read()
            if len(label) > 1:
                if label[0] == '0':
                    shutil.copy2(f'../CNN/BurnsDataSet/img{x}.jpg', f'../CNN/BurnsDataSet/Label 0/img{x}.jpg')
                    print(f'{x} : label 0')
                if label[0] == '1':
                    shutil.copy2(f'../CNN/BurnsDataSet/img{x}.jpg', f'../CNN/BurnsDataSet/Label 1/img{x}.jpg')
                    print(f'{x} :label 1')
                if label[0] == '2':
                    shutil.copy2(f'../CNN/BurnsDataSet/img{x}.jpg', f'../CNN/BurnsDataSet/Label 2/img{x}.jpg')
                    print(f'{x} : label 2')
    else:
        print('File does not exist')
