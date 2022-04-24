from socket import gethostbyname
from requests import get
from response import Response

class QueryError(Exception):
    pass

class Querier:
    _URL: str = "https://cdn.rage.mp/master/"
    
    def __init__(self, host: str, port: int = None) -> None:
        self.port: int = port or 22005
        self.host: str = (host + ":" + str(port), gethostbyname(host) + ":" + str(port))
        
    def info(self) -> Response:
        query_list: dict = get(self._URL).json()
        
        try:
            if self.host[0] in query_list:
                data = self.parse_response(query_list[self.host[0]])
                return data
            elif self.host[1] in query_list:
                data = self.parse_response(query_list[self.host[1]])
                return data
            else:
                raise QueryError("Server not found in masterlist.")
        except Exception as e:
            raise QueryError(f"Failed to query: '{e}'")
        
    @staticmethod
    def parse_response(data: str) -> Response:
        response: Response = Response()
        response.name = data["name"]
        response.gamemode = data["gamemode"]
        response.url = data["url"]
        response.lang = data["lang"]
        response.players = data["players"]
        response.maxplayers = data["maxplayers"]
        response.peak = data["peak"]
        return response