# saves all enabled laters to outDir

import ogr,os
outDir = 'C:/path/to/output/directory/'

if os.path.exists(outDir) == False:
    print("Path does not exist")
else:
    for vLayer in iface.mapCanvas().layers():
        if vLayer.type()==0: #Save only shapefiles in the Layer Panel 
            layerPath = vLayer.dataProvider().dataSourceUri()
            layerFileName = os.path.split(layerPath)[1].split('|')[0]
            if not os.path.exists(outDir + layerFileName):
                QgsVectorFileWriter.writeAsVectorFormat(vLayer, outDir + layerFileName, "utf-8", vLayer.crs(),  "ESRI Shapefile")            
                print(vLayer.name() + " saved successfully as " + outDir + layerFileName)
