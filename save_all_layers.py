# saves all enabled laters to outDir

import ogr,os
outDir = 'C:\your_output_folder_here\\'

if os.path.exists(outDir) == False:
    print("Path does not exist")
else:
    for vLayer in iface.mapCanvas().layers():
        if vLayer.type()==0: #Save only shapefiles in the Layer Panel 
            layerPath = vLayer.dataProvider().dataSourceUri()
            layerFileName = os.path.split(layerPath)[1].split('|')[0]
            QgsVectorFileWriter.writeAsVectorFormat(vLayer, outDir + layerFileName, "utf-8", vLayer.crs(),  "ESRI Shapefile")            
            print(vLayer.name() + " saved successfully as " + outDir + layerFileName)
            
            
            
            
            
'''
import ogr,os
outDir = 'C:\GEOS_COURSEWORK\geos2400\A2\submission\\'

print os.path.exists("C:\\")

for vLayer in iface.mapCanvas().layers():
    if vLayer.type()==0: #Save only shapefiles in the Layer Panel 
        layerPath = vLayer.dataProvider().dataSourceUri()
        layerFileName = os.path.split(layerPath)[1].split('|')[0]
        print(os.path.exists(outDir + layerFileName))
        print(outDir + layerFileName)
        #print(layerFileName)
'''        
