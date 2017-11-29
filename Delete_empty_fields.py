from PyQt4.QtCore import QDate, QDateTime

lyr = iface.activeLayer()
lstDelete = []

for idx in lyr.dataProvider().attributeIndexes():
    uv = lyr.dataProvider().uniqueValues( idx )
    if len( uv ) == 1:
        if uv[0] == NULL or uv[0] == QDateTime() or uv[0] == QDate() or uv[0] == '':
            lstDelete.append( idx )

if not lyr.dataProvider().capabilities() & QgsVectorDataProvider.DeleteFeatures:
    print "This layer provider does not support deleting attributes."
else:
    lyr.dataProvider().deleteAttributes( lstDelete )
    lyr.updateFields() # Update the layer structure