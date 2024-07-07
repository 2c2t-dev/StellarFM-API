import json

class CacheManager:
    def __init__(self):
        self.cache = json.loads(open("cache.json", encoding="utf-8").read())
    
    def is_exist(self, title: str) -> bool:
        exist = False
        for track in self.cache:
            if track['title'] == title:
                exist = True
                break
        return exist
    
    def get(self, title: str) -> str:
        for track in self.cache:
            if track['title'] == title:
                return track['image']
        return None
    
    def add(self, title: str, image: str) -> None:
        self.cache.append({
            "title": title,
            "image": image
        })
        self.save()

    def save(self) -> None:
        with open("cache.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(self.cache, indent=4))