from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import sys

def run(image):
	app = ClarifaiApp(api_key='2b9c795fe5814ccaa072c31173004037')

	model = app.models.get("Banana")

	initPath = './Fruits/Bananas/Test/'

	input = image["inputtedBanana"]

	fileName = (initPath + input)

	img = ClImage(filename=fileName)
	# predict with the model
	JSON_Model = model.predict([img])

	predictions = JSON_Model["outputs"][0]["data"]["concepts"]

	#for p in predictions:
	#	print(p["name"] + " " + str(p['value']))

	#response = str(input("Do you agree with this? Y/N"))
	stage = predictions[0]["name"]
	stageNum = int(predictions[0]["name"][11:])
	app.inputs.create_image_from_filename(filename=fileName, concepts=[stage], not_concepts=[predictions[4]["name"]])
	#if (response == "Y"):
	#	stageNum = int(predictions[0]["name"][11:])
	#
	#	app.inputs.create_image_from_filename(filename=fileName, concepts=[stage],
	#										  not_concepts=[predictions[4]["name"]])
	#else:
	#	stageNum = int(input("What stage would you rate this banana(1-5): "))
	#	stage = "BananaStage" + str(stageNum)
	#	app.inputs.create_image_from_filename(filename=fileName, concepts=[stage])

	model.train()

	return stageNum

#run()