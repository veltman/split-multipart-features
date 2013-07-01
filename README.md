Split Multipart Features in QGIS
========================

*A script for selectively splitting up multipart features in QGIS.*

As far as I can tell, there's no good way to split a selected multipart feature into its constituent parts in QGIS.  If you have, say, a chain of islands that is stored as a single MultiPolygon feature, and you want each island to be its own feature, this doesn't seem to be possible in the GUI (if it is and I just can't figure it out, tell me!).

To solve this problem, I created this script, based on Alexandre Neto's solution:

http://gis.stackexchange.com/questions/44799/how-to-transform-a-selected-multipart-feature-into-singlepart-features-while-edi

His version is also available as a plugin, which I couldn't get to work, but YMMV:

http://plugins.qgis.org/plugins/splitmultipart/

I've included the script in two versions: plain and a ScriptRunner version which adds some extra wrapping to make it work with the very useful ScriptRunner QGIS plugin:

http://plugins.qgis.org/plugins/scriptrunner/

It should be easily modifiable to do other helpful things as it splits, like skipping any new features that would be smaller than a certain area, or skipping features that would be outside a bounding box.
