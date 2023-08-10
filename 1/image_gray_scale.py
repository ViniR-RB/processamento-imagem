import cv2

image_path = 'eu.jpeg'
image = cv2.imread(image_path)

if image is None:
    print("Não foi possível carregar a imagem.")
else:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Exibir a imagem em escala de cinza
    cv2.imshow('Imagem em Escala de Cinza', gray_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()