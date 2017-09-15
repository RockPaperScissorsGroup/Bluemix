import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='38101248a17c138c02f3e9c20052f04af5b3a61a')
# {38101248a17c138c02f3e9c20052f04af5b3a61a}
# print(json.dumps(visual_recognition.classify(images_file='SteinTest.jpg'), indent = 2))


car_path = join(dirname(__file__), 'images/SteinTest.jpg')
with open(car_path, 'rb') as images_file:
    car_results = visual_recognition.classify(images_file=images_file,
                                              classifier_ids=[
                                                  'schnickschnackschnuck_699533305'])
    print(json.dumps(car_results, indent=2))