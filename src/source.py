class Source:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def __repr__(self):
        return f"<Source(id={self.id}, name={self.name})>"