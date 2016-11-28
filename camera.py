from picamera import PiCamera
from time import sleep
from openalpr import Alpr

class Camera:
	def __init__(self):
		camera = PiCamera()
	    camera.rotation = 180
	    camera.hflip = True

	def recognizePlate():
	    camera.capture('images/1.jpg')
	    alpr = Alpr("us", "/etc/openalpr/openalpr.conf", "/usr/share/openalpr/runtime_data")
	    if not alpr.is_loaded():
	        print("Error loading OpenALPR")
	        sys.exit(1)

	    alpr.set_top_n(20)
	    alpr.set_default_region("md")

	    results = alpr.recognize_file("images/1.jpg")

	    nPos = 2
	    sepPos = [400, 800]
	    tmpPlate = {}
	    i = 0
	    for plate in results['results']:
	        i += 1
	        x = plate['coordinates'][0]['x']
	        number = plate['candidates'][0]['plate']
	        tmpPlate[x] = number
	        print("Plate #%d, (%d,%d)(%d,%d)" % (i , plate['coordinates'][0]['x'], plate['coordinates'][0]['y'], plate['coordinates'][1]['x'], plate['coordinates'][1]['y']))
	        print("   %12s %12s" % ("Plate", "Confidence"))
	        for candidate in plate['candidates']:
	            print(" %12s%12f" % (candidate['plate'], candidate['confidence']))

	    sortedKey = sorted(tmpPlate)
	         
	    res = {1:"", 2:"", 3:""}
	    nPlate = len(tmpPlate)
	    
	    pos = 0
	    keyIndex = 0
	    while pos < nPos and keyIndex < nPlate:
	        if sepPos[pos] > sortedKey[keyIndex]:
	            res[pos+1] = tmpPlate[sortedKey[keyIndex]]            
	            keyIndex += 1    
	        pos += 1

	    while keyIndex < nPlate:
	        res[pos + 1] = tmpPlate[sortedKey[keyIndex]]
	        keyIndex += 1
	        pos += 1
	    #alpr.unload()
	    print(res)
	    return res

