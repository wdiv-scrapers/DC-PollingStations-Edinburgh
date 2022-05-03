

from dc_base_scrapers.geojson_scraper import GeoJsonScraper

stations_url = "https://edinburghcouncilmaps.info/arcgis/rest/services/Misc/INSPIRE/MapServer/7/query?outFields=*&where=1%3D1&f=geojson"
districts_url = "https://edinburghcouncilmaps.info/arcgis/rest/services/Misc/INSPIRE/MapServer/28/query?outFields=*&where=1%3D1&f=geojson"
council_id = 'EDH'

stations_scraper = GeoJsonScraper(stations_url, council_id, 'utf-8', 'stations', key='OBJECTID')
stations_scraper.scrape()
districts_scraper = GeoJsonScraper(districts_url, council_id, 'utf-8', 'districts', key='OBJECTID')
districts_scraper.scrape()