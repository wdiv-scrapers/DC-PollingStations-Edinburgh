

from dc_base_scrapers.geojson_scraper import GeoJsonScraper

stations_url = "https://opendata.arcgis.com/datasets/1650151797b64252bbdc9afe40041749_7.geojson"
districts_url = "https://opendata.arcgis.com/datasets/e56a3c00197543caaeb161aeffc9c3ec_28.geojson"
council_id = 'EDH'

stations_scraper = GeoJsonScraper(stations_url, council_id, 'utf-8', 'stations', key='OBJECTID')
stations_scraper.scrape()
districts_scraper = GeoJsonScraper(districts_url, council_id, 'utf-8', 'districts', key='OBJECTID')
districts_scraper.scrape()