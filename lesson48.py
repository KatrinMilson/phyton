import os.path
import zipfile

phyton_path = 'C:\\Users\\satoa\\OneDrive\\Рабочий стол\\phyton'
zip_path = 'C:\\Users\\satoa\\OneDrive\\Рабочий стол\\phyton\\test.zip'
zip_name = 'test.zip'
my_zip = zipfile.ZipFile(zip_path, 'w')

for phyton, subphyton, files in os.walk(phyton_path):
    # print(phyton, file)
    for file in files:
        if file == zip_name:
            continue
        my_zip.write(os.path.join(phyton, file),
                     os.path.relpath(os.path.join(phyton, file), phyton_path),
                     compress_type=zipfile.ZIP_DEFLATED)

my_zip.close()
