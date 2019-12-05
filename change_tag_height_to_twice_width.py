import xml.dom.minidom
import os

file_list = os.listdir("./")
file_list_xml = [file for file in file_list if file.endswith(".xml")]
print ("file_list_xml: {}".format(file_list_xml))

for file_xml in file_list_xml:
    resulPath = "./result/" + file_xml
    doc = xml.dom.minidom.parse(file_xml)
    person = doc.getElementsByTagName("object")
    print("person size:%d" % person.length)
    name = doc.getElementsByTagName("name")
    xmin = doc.getElementsByTagName("xmin")
    xmax = doc.getElementsByTagName("xmax")
    ymin = doc.getElementsByTagName("ymin")
    ymax = doc.getElementsByTagName("ymax")

    for idx in range(0, xmin.length):
        print("name:%s" % name[idx].firstChild.nodeValue)
        width = int(xmax[idx].firstChild.nodeValue) - int(xmin[idx].firstChild.nodeValue)
        height = int(ymax[idx].firstChild.nodeValue) - int(ymin[idx].firstChild.nodeValue)
        print("width:%d, height:%d" % (width, height))
        if height > width * 2:
            ymax[idx].firstChild.nodeValue = str(width * 2 + int(ymin[idx].firstChild.nodeValue))
            print("change ymax:%s" % ymax[idx].firstChild.nodeValue)
            if not os.path.exists(os.path.dirname(resulPath)):
                try:
                    os.makedirs(os.path.dirname(resulPath))
                except OSError as exc: # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise
            with open(resulPath,'w') as f:
                f.write(doc.toxml())
        else:
            continue