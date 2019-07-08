import boto3

photo ='imagename'

client = boto3.client('rekognition')
with open(photo, 'rb') as source_image:
	source_bytes = source_image.read()


#detect images from local storage.
detectinglabels = client.detect_labels(Image={'Bytes': source_bytes},MaxLabels=2,MinConfidence=95)

#detect images from S3 buckets.
###detectinglabels = client.detect_labels(Image={'S3Object':{'Bucket':'bucketname','Name':photo}},MaxLabels=2,MinConfidence=95)


print(detectinglabels)
#Get values from S3 images:
###print(detectinglabels)

detectingmoderationlabels = client.detect_moderation_labels(Image={'Bytes': source_bytes},MinConfidence=75)
print("--------------------------------------------------------------")
print(detectingmoderationlabels)


detectingfacialanalysis = client.detect_faces(Image={'Bytes': source_bytes},Attributes =['ALL']) 
print("----------------------------------------------------------------")
for key, value in detectingfacialanalysis.items():
	if key == 'FaceDetails':
		for people_attr in value:
			print(people_attr)
			print("=========")

detectingcelebraties = client.recognize_celebrities(Image={'Bytes': source_bytes})
print("----------------------------------------------------------------")
for key, value in detectingcelebraties.items():
	if key =='CelebrityFaces':
		for people in value:
			print(people)

facecomparision = client.compare_faces(
	SourceImage={
	'S3Object':{
	      'Bucket':'bucketname',
	      'Name': 'image1.jpeg'
	}
	},
	TargetImage={
	     'S3Object': {
	        'Bucket':'bucketname',
	        'Name': 'image2.jpeg'
	     }
	},
)
print("----------------------------------------------------------------")
for key, value in facecomparision.items():
	if key in ('FaceMatches','UnmatchedFaces'):
		print(key)
		for att in value:
			print(att)


textrecognition = client.detect_text(Image={'Bytes': source_bytes})
print("-----------------------------------------------------------------")
print(textrecognition)
