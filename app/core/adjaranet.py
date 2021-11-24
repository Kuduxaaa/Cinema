# -*- coding: utf-8 -*-
# Coded By Kuduxaaa

import requests
import json

from app import app

class Api:
    def __init__(self):
        '''
        Initialize Api class
        '''
        
        self.base_url = app.config.get('API_URL')
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'googlebot'
        })
       
        

    def getMovies(self,
                  language = 'geo',
                  per_page = 20,
                  page = 1) -> list:
        '''
        Getting movies
        '''
        
        lang = language[:3].upper()
        url = self.generateFilteredURL(f'{self.base_url}/movies?page={page}&per_page={per_page}&source=adjaranet', {
            'language': lang,
            'sort': '-upload_date'
        })    
        
        response = self.session.get(url)
        return json.loads(response.text)
    
    
    
    def searchMovie(self, keyword: str) -> list:
        '''
        Search movie with keyword
        '''
        
        response = self.session.get(f'{self.base_url}/search?keywords={keyword}&source=adjaranet')
        return json.loads(response.text)
    
    

    def getMovieDetails(self, movieId) -> list:
        '''
        Get detailed information about movie
        '''
        
        response = self.session.get(f'{self.base_url}/movies/{movieId}?source=adjaranet')
        return json.loads(response.text)
    
    
    
    def getSerials(self,
                  language = 'geo',
                  per_page = 20,
                  page = 1) -> list:
        '''
        Getting serials
        '''
        
        lang = language[:3].upper()
        url = self.generateFilteredURL(f'{self.base_url}/movies?page={page}&per_page={per_page}&source=adjaranet', {
            'language': lang,
            'sort': '-upload_date',
            'type': 'series'
        })
        
        response = self.session.get(url)
        return json.loads(response.text)
    
    
    
    def getMovieFiles(self,
                     movieLongId,
                     seasonId):
        '''
        Getting media files data
        '''
        
        response = self.session.get(f'{self.base_url}/movies/{movieLongId}/season-files/{seasonId}?source=adjaranet')
        return json.loads(response.text)
    
    
    def getCategoryList(self):
        '''
        Getting category list with id
        '''
        
        response = self.session.get(f'{self.base_url}/genres?source=adjaranet')
        return json.loads(response.text)
    
    
    
    
    def generateFilteredURL(self, 
                            url: str, 
                            filters: dict = {}) -> list:
        '''
        Generating filters in URL
        '''
        
        url = f'{url}?source=adjaranet' if '?' not in url else url
            
        for filter in filters:
            url = f'{url}&filters[{filter}]={filters[filter]}&'
            
        return url[:(len(url) - 1)]