class Message:
    """Representing the message that should be passed between nodes. This class is a simple data-holder which
    contains the required data to be transferred between nodes. """
    #def __init__(self,node_id,yi,zi):
    def __init__(self,node_id,xi):
        self.node_id=node_id
        self.xi = xi
        #self.yi=yi
        #self.zi=zi