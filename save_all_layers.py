# saves all enabled laters to outDir

import ogr,os
outDir = 'C:\your_output_folder_here\\'

if os.path.exists(outDir) == False:
    print("Path does not exist")
else:
    for vLayer in iface.mapCanvas().layers():
        if vLayer.type()==0: #Save only shapefiles in the Layer Panel 
            QgsVectorFileWriter.writeAsVectorFormat(vLayer, outDir + vLayer.name() + ".shp", "utf-8", vLayer.crs(),  "ESRI Shapefile")
            print(vLayer.name() + " saved successfully")
