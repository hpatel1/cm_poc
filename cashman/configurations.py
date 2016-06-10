"""
Site(Build) version
"""
VERSION = "1.0"
BUILD_VERSION = "cashman " + VERSION

"""
Choose Environment from 'production', 'staging', 'development'
"""
ENV = "developement"


"""
Add functionalities from following list to SERVER_TYPE List -
'admin' - Admin panel
'api' - API server
'views' - Only Pages
'supplier' - supplier portal
'media' - Media files
"""
SERVER_TYPE = ['admin', 'api', 'views', 'supplier', 'static']
