import os
import shutil
import zipfile

code_path = os.getcwd() + '/input_code.txt'
chn_path = os.getcwd() + '/changed_opening'
base_path = os.getcwd()

chasi_code = []

with open(code_path, "r") as file:
    strings = file.readlines()

for idx in range(len(strings)):
    chasi_code.append( strings[idx].replace('\n', ''))


def createFolder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print('폴더 생성')
    else:
        # 해당 디렉토리 삭제
        shutil.rmtree(r'%s' %chn_path)
        print('폴더 삭제')
 

createFolder('./changed_opening')

def createDir(dir):
    os.makedirs('changed_opening/' + dir)


for jdx in range(len(chasi_code)):
    createDir(chasi_code[jdx])
    print(chasi_code[jdx], '폴더 생성 완료')

opening_dir = base_path + '/opening'
changed_dir = base_path + '/changed_opening'
reading_dir = base_path + '/reading'

opening_list = os.listdir(opening_dir)

reading_list = os.listdir(reading_dir)
changed_list = os.listdir(changed_dir)

for kdx in range(len(changed_list)):
    createDir(chasi_code[kdx] + '/' + chasi_code[kdx] + '_01')
    createDir(chasi_code[kdx] + '/' + chasi_code[kdx] + '_02')
    
for kdx, val in enumerate(changed_list):
   
    change_path = chn_path + '/' + val
    change_list = os.listdir(change_path)

    for ldx, wal in enumerate(change_list):
        if '_01' in wal:
            for dir in range(6):
                if dir == 2:
                    shutil.copy(opening_dir + '/' + opening_list[dir], chn_path + '/' + changed_list[kdx] + '/' + change_list[ldx] + '/' + opening_list[dir])
                else: 
                    shutil.copytree(opening_dir + '/' + opening_list[dir], chn_path + '/' + changed_list[kdx] + '/' + change_list[ldx] + '/' + opening_list[dir])
  
        else:
            for dir in range(6):
                if  dir == 3:
                    shutil.copy(reading_dir + '/' + reading_list[dir], chn_path + '/' + changed_list[kdx] + '/' + change_list[ldx] + '/' + reading_list[dir])
                else:
                    shutil.copytree(reading_dir + '/' + reading_list[dir], chn_path + '/' + changed_list[kdx] + '/' + change_list[ldx] + '/' + reading_list[dir])



owd = os.getcwd()
print('모든 폴더 생성 완료')

def zip_all_dir(need_dir):
    os.chdir(chn_path)
    fantasy_zip = zipfile.ZipFile( base_path + '/finish_zip/' + need_dir + '.zip', 'w')
    
    for folder, subfolders, files in os.walk(chn_path + '/' + need_dir):
        for file in files:
            fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), chn_path + '/' + need_dir), compress_type = zipfile.ZIP_DEFLATED)
    fantasy_zip.close()
    os.chdir(owd)


def print_asking():
    print('----------------------------')
    print('모든 폴더를 압축 하시겠습니까?')
    print('Yes = 1 입력', 'No = 2 입력')


def ask_fix():
    print_asking()
    asking = input()
    if asking == '1':
        for kdx in range(len(changed_list)):
            zip_all_dir(changed_list[kdx])
            print(changed_list[kdx] + ' 압축 완료')
    else:
        ask_fix();

ask_fix()
print('모든 폴더 압축 완료')