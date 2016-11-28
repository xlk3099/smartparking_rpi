from picamera import PiCamera
from time import sleep
from openalpr import Alpr

def recognizePlate():
    camera = PiCamera()
    camera.rotation = 180
    camera.hflip = True
    camera.start_preview()
    camera.capture('images/1.jpg')
    camera.stop_preview()

    alpr = Alpr("us", "/etc/openalpr/openalpr.conf", "/usr/share/openalpr/runtime_data")
    if not alpr.is_loaded():
        print("Error loading OpenALPR")
        sys.exit(1)

    alpr.set_top_n(20)
    alpr.set_default_region("md")

    results = alpr.recognize_file("images/1.jpg")

    res = {1:"", 2:"",3:""}
    i = 0
    for plate in results['results']:
        i += 1
        res[i] = plate['candidates'][0]['plate']
        print("Plate #%d, (%d,%d)" % (i , plate['coordinates'][0]['x'], plate['coordinates'][0]['y']))
        print("   %12s %12s" % ("Plate", "Confidence"))
        for candidate in plate['candidates']:
            print(" %12s%12f" % (candidate['plate'], candidate['confidence']))

    #alpr.unload()
    print(res)
    return res

result = recognizePlate()
print("This should work")
print(result)
