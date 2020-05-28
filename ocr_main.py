import cv2
import numpy as np
import requests
import io
import json

img = cv2.imread("test.jpg")


# Crop your image of needed
height, width, _ = img.shape
# roi = img[0: height, 400: width]
roi = img

# Ocr
url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode("test.jpg", roi, [1, 90])
file_bytes = io.BytesIO(compressedimage)


#Remember to change your API Key, if you don't have it register @api.ocr
result = requests.post(url_api,
              files = {"test.jpg": file_bytes},
              data = {"apikey": "YOUR_KEY",
                      "language": "eng"})

result = result.content.decode()
result = json.loads(result)

parsed_results = result.get("ParsedResults")[0]
text_detected = parsed_results.get("ParsedText")
print(text_detected)

cv2.imshow("roi", roi)
cv2.imshow("Img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()