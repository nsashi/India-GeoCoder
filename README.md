# Welcome to India GeoCoder!
**India GoeCoder** is a plugin on _QGIS 3_ to help users geocode health data from NRHM website (https://nrhm-mis.nic.in/hmisreports/frmstandard_reports.aspx) and later visualise the same by displaying data on a map and exporting the map in the form of an image.

This plugin is developed specifically for Indian health data collected by Ministry of Health & Family Welfare, Government of India under the digital initiative of National Health Mission. The data is released under **Health Management Information System** and is openly available at NRHM (National Rural Health Mission) website: https://nrhm-mis.nic.in/hmisreports/frmstandard_reports.aspx. This data comprises of around *200* health indicators collected across over *5,000* sub districts.



## Deploying India GeoCoder plugin in QGIS 3.2
There are various methods for deploying India GeoCoder plugin in QGIS 3.2. But first, you will need to know the location of *plugins* directory on your system. For that,

* Open QGIS application.
* Click the **Settings** menu.
* Inside **User Profiles**, click **Open Active Profile Folder**.

This is the **QGIS plugins folder** where all your installed plugins appear.

Now to install **India GeoCoder** plugin:

1. Step 1: Download this repository and rename the folder as **indiageocoder**
2. Step 2: Copy the indiageocoder folder in the QGIS plugins folder.
3. Step 3: Now in QGIS 3, go to **Manage and Install Plugins…** in the **Plugins** menu.
4. Step 4: Click the **Installed** tab in the dialog box that appears.
5. Step 5: Select **India GeoCoder** from the list view in the dialog and install it.

![Dialog](https://github.com/yashdeep01/India-GeoCoder/blob/master/Screenshots/Installed_plugins_dialog.png)
 
If you received the plugin as a zip file, instead of clicking **Installed** tab in the **Plugins** dialog, select **Install from ZIP** tab and give the path of the zip file.


#### Note:
Spatial data for geocoding and visualisation is provided in the repository as **All.gpkg**. This is a district level geopackage file of India. Non-spatial data should be downloaded from **Performance of Key HMIS Indicators(upto District Level)** section of the NRHM website. This directory should be given as input in the first dialog while ***Loading and Joining Data***. A folder containing sample health data for district is given in the repository for reference and testing purposes. User may use *this* as the input directory discussed above.

![Dialog](https://github.com/yashdeep01/India-GeoCoder/blob/master/Screenshots/Input_directory.png)


## Dependencies
India GeoCoder relies on the following modules. User *must* have them installed before running the plugin.

* pandas
* BeautifulSoup
* csv
