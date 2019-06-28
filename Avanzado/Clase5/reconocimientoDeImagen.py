import json
from ibm_watson import VisualRecognitionV3

#Fecha de la versión
visual_recognition = VisualRecognitionV3('2018-03-19', iam_apikey = 'RtlQNoyXTKIdRrAclZNku7OKD8fgdK7s9uPEkjJxvHu_')

with open('./lore.jpg', 'rb') as image_file:
	faces = visual_recognition.detect_faces(image_file).get_result()
print(json.dumps(faces, indent = 2))

"""
{
  "images": [
    {
      "faces": [
        {
          "age": {
            "min": 14,
            "max": 16,
            "score": 0.9997695
          },
          "face_location": {
            "height": 284,
            "width": 187,
            "left": 255,
            "top": 70
          },
          "gender": {
            "gender": "FEMALE",
            "gender_label": "female",
            "score": 0.9999957
          }
        }
      ],
      "image": "hannah.jpg"
    }
  ],
  "images_processed": 1
}
"""