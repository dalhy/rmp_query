class Response:
    def __init__(self):
        self.name: str = ""
        self.gamemode: str = ""
        self.url: str = ""
        self.lang: str = ""
        self.players: int = 0
        self.maxplayers: int = 0
        self.peak: int = 0
        
    def __str__(self):
        return f'<Response name="{self.name}" gamemode="{self.gamemode}" url="{self.url}" lang="{self.lang}" players={self.players} maxplayers={self.maxplayers} peak={self.peak}>'