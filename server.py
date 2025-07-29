import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/deezerdevs/api/deezer-1'

mcp = FastMCP('deezer-1')

@mcp.tool()
def infos() -> dict: 
    '''Get the infos about the api in the current country'''
    url = 'https://deezerdevs-deezer.p.rapidapi.com/infos'
    headers = {'x-rapidapi-host': 'deezerdevs-deezer.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def radio(id: Annotated[str, Field(description='The radio deezer ID')]) -> dict: 
    '''A radio object'''
    url = 'https://deezerdevs-deezer.p.rapidapi.com/radio/%7Bid%7D'
    headers = {'x-rapidapi-host': 'deezerdevs-deezer.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def genre(id: Annotated[str, Field(description="The editorial's Deezer id")]) -> dict: 
    '''A genre object'''
    url = 'https://deezerdevs-deezer.p.rapidapi.com/genre/%7Bid%7D'
    headers = {'x-rapidapi-host': 'deezerdevs-deezer.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search(q: Annotated[str, Field(description='')]) -> dict: 
    '''Search tracks'''
    url = 'https://deezerdevs-deezer.p.rapidapi.com/search'
    headers = {'x-rapidapi-host': 'deezerdevs-deezer.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def playlist(id: Annotated[str, Field(description="The playlist's Deezer id")]) -> dict: 
    '''A playlist object'''
    url = 'https://deezerdevs-deezer.p.rapidapi.com/playlist/%7Bid%7D'
    headers = {'x-rapidapi-host': 'deezerdevs-deezer.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def artist(id: Annotated[str, Field(description="The artist's Deezer id")]) -> dict: 
    '''An artist object'''
    url = 'https://deezerdevs-deezer.p.rapidapi.com/artist/%7Bid%7D'
    headers = {'x-rapidapi-host': 'deezerdevs-deezer.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def editorial(id: Annotated[str, Field(description="The editorial's Deezer id")]) -> dict: 
    '''An editorial object'''
    url = 'https://deezerdevs-deezer.p.rapidapi.com/editorial/%7Bid%7D'
    headers = {'x-rapidapi-host': 'deezerdevs-deezer.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def track(id: Annotated[str, Field(description="The track's Deezer id")]) -> dict: 
    '''A track object'''
    url = 'https://deezerdevs-deezer.p.rapidapi.com/track/%7Bid%7D'
    headers = {'x-rapidapi-host': 'deezerdevs-deezer.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def comment(id: Annotated[str, Field(description="The playlist's Deezer id")]) -> dict: 
    '''A comment object'''
    url = 'https://deezerdevs-deezer.p.rapidapi.com/comment/%7Bid%7D'
    headers = {'x-rapidapi-host': 'deezerdevs-deezer.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def album(id: Annotated[str, Field(description='The Deezer album id')]) -> dict: 
    '''An album object'''
    url = 'https://deezerdevs-deezer.p.rapidapi.com/album/%7Bid%7D'
    headers = {'x-rapidapi-host': 'deezerdevs-deezer.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
