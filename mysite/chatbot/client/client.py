import Pyro5.api

class ChatBotClient:
    def __init__(self) -> None:
        pass

    def get_conneciton(self):
        return Pyro5.api.Proxy("PYRO:ChatBot@host.docker.internal:43778")
    
    def infer(self, content)-> tuple[str, str]:
        return self.get_conneciton().chat(content)
