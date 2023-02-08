import subprocess
import os

class Database:
    def __init__(self) -> None:
        pass
    
    def update(self, url:str, output:str):
        subprocess.run(["wget", url, "-O", output])