from json import dump
class Pather:
    def __json__(self, ___path, ___data=dict):
        try:
            with open(___path, 'w') as file_worker : dump(___data, file_worker)
        except : return False
        finally : return True
    def __html__(self, ___path, ___data):
        try:
            with open(___path, "w") as file_worker : file_worker.write(___data)
        except : return False
        finally : return True
