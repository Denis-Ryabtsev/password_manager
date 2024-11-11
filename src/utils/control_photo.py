import cv2


# Проверка схожести фото
def comparison_photo() -> list[int]:
    input_image = cv2.imread('input_photo.jpg')
    database_image = cv2.imread('database_input_photo.jpg')
    # Converting images to histograms
    histogram1 = cv2.calcHist([input_image], [0], None, [256], [0, 256])
    histogram2 = cv2.calcHist([database_image], [0], None, [256], [0, 256])
    # Calculating Histogram Similarity Using Chi-Square Method
    return cv2.compareHist(histogram1, histogram2, cv2.HISTCMP_CHISQR)

# Проверка качества фото
def check_photo(file: object) -> int:
    image = cv2.imread(file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    laplacian = cv2.Laplacian(blur, cv2.CV_64F).var()
    return laplacian

# Проверка наличие лица на фото
def check_face_photo(file: object) -> bool:
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    image = cv2.imread(file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, 
        scaleFactor=1.1,
        minNeighbors=4,
        minSize=(75, 75)
    )
    if len(faces) < 1:
        return False
    else:
        return True