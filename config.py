from pathlib import Path


class Envs:

    @staticmethod
    def get_ranks_env() -> str:
        return  '\n'.join(Path("envs/ranks.env").read_text().splitlines())
    
    @staticmethod
    def get_wegro_env() -> str:
        return  '\n'.join(Path("envs/wegro.env").read_text().splitlines())



class Credential:

    @staticmethod
    def get_sheba_dev() ->str:
        return '\n'.join(Path("credentials/sheba.db").read_text().splitlines())