import os

import cv2


def main():
    path = 'images/'
    data_path = os.path.join(os.path.dirname(cv2.__file__), 'data')
    face_cascade = cv2.CascadeClassifier(os.path.join(data_path, 'haarcascade_frontalface_default.xml'))
    files_list = os.listdir(path)
    length = len(files_list)
    i = 0
    for file in files_list:
        image = cv2.imread(file)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.05, 5)
        if len(faces) > 0:
            print("Görüntüde yüz bulundu.")
        else:
            print("Görüntüde yüz bulunamadı.")
            os.remove(path + file)
        i += 1
        print(str(i) + "/" + str(length) + " işlendi.")


if __name__ == '__main__':
    main()
