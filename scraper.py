

from dc_base_scrapers.geojson_scraper import GeoJsonScraper

stations_url = "https://opendata.arcgis.com/datasets/89c67161768d432e88982da59af3d093_7.geojson"
districts_url = "https://opendata.arcgis.com/datasets/2cee9b18a21344b0879c3c51d71fd2c6_28.geojson"
council_id = 'EDH'

stations_scraper = GeoJsonScraper(stations_url, council_id, 'utf-8', 'stations', key='OBJECTID_1')
stations_scraper.scrape()
districts_scraper = GeoJsonScraper(districts_url, council_id, 'utf-8', 'districts', key='OBJECTID')
districts_scraper.scrape()
