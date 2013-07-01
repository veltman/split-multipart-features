from qgis.core import *
from PyQt4.QtCore import *
import qgis.utils

def run_script(iface):
	"""
		Will break any SELECTED multipart feature into separate features
		in QGIS.  Defined inside of run_script to be used with the ScriptRunner plugin:

		http://spatialgalaxy.net/2013/03/18/new-version-of-the-qgis-script-runner-plugin/

		But you could just run the same code separately if you prefer.

		Two commented lines add attributes for the centroid X and Y of the feature being created,
		which can be helpful for pruning and merging when you're dealing with tiny geometries.
		Ex: If you broke Canada up into its constituent geometries, you'd end up with hundreds,
		maybe thousands of tiny Arctic islands.  Another useful modification might be to set
		the total AREA of the new geometry as an attribute.
	"""
	layer = qgis.utils.iface.mapCanvas().currentLayer()
	
	# Features to remove
	remove_list = []

	# Loop through selected features
	for feature in layer.selectedFeatures():		
		geom = feature.geometry()

		# If it is a multipart feature...
		if geom.isMultipart():

			# Add it to be removed at the end
			remove_list.append(feature.id())

			# Empty list of new features
			new_features = []

			# Create a temporary feature with the same attributes as the original
			temp_feature = QgsFeature(feature)

			# For each part of the geometry
			for part in geom.asMultiPolygon():				
				
				# Try to create a new feature, some weird geometries break this, currently they are skipped
				try:
					# Create new polygon for new feature, add it to list of new features
					newPolygon = QgsGeometry.fromPolygon(part)
					temp_feature.setGeometry(newPolygon)					
					# temp_feature.addAttribute(2,newPolygon.centroid().asPoint().x())
					# temp_feature.addAttribute(3,newPolygon.centroid().asPoint().y())
					new_features.append(QgsFeature(temp_feature))					
				except:
					print "failed"

			# Add all new features found
			layer.addFeatures(new_features, False)

		# Remove the original features
		if len(remove_list) > 0 and len(new_features) > 0:			
			for id in remove_list:
				layer.deleteFeature(id)