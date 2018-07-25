Plugin Builder Results

Your plugin IndiaGeocoder was created in:
    /Users/yashdeep/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/indiageocoder

Your QGIS plugin directory is located at:
    /Users/yashdeep/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins

What's Next:

  * Copy the entire directory containing your new plugin to the QGIS plugin
    directory

  * Compile the resources file using pyrcc5

  * Run the tests (``make test``)

  * Test the plugin by enabling it in the QGIS plugin manager

  * Customize it by editing the implementation file: ``india_geocoder.py``

  * Create your own custom icon, replacing the default icon.png

  * Modify your user interface by opening IndiaGeocoder.ui in Qt Designer

  * You can use the Makefile to compile your Ui and resource files when
    you make changes. This requires GNU make (gmake)

For more information, see the PyQGIS Developer Cookbook at:
http://www.qgis.org/pyqgis-cookbook/index.html

(C) 2011-2018 GeoApt LLC - geoapt.com

From the developer (Yashdeep):

  * The paths given above are specific for my system (Mac OS X). Yours may be different.
    Open Active Profile Folder in Settings > python > plugins > indiageocoder
  
  * Plugin reloader is a must.

  * 'pb_tool compile' was a convenient terminal command for me to compile resources and UI files in one go.

  * india_geocoder_dialog.py has all the classes for dialog boxes of the plugin.

  * All.gpgk is the spatial data (block level) used for joining. It is inside 'indiageocoder' folder.
    Its key field used for joining is 'ID' (subdistrict_district_state)

  * temp.csv and temp.csvt are generated whenever 'Load and Join Data' runs. It is the appended version of all xls files present in the directory input in a simplified format. Its key field is named 'ID' too.

  * For reference, 2 sample folders of HMIS data are given – 'Sample District level' & 'Sample sub district level'.
    These can be used for testing as well.

  * Should the xls table format given by NRHM change in the future, do alterations in parse_html_table() in ``india_geocoder.py``

