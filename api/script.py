import json, random, os

class JsonService:
    @staticmethod
    def get_people(namePerson: str) -> dict:
        try:
            if not os.path.isfile(f"api/json/conversations/{namePerson}.json"):
                return {}
                
            with open(f"api/json/conversations/{namePerson}.json", "r", encoding="utf-8") as f:
                return json.load(f)
        
        except json.JSONDecodeError:
            return {}
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")
            return {}
    
    @staticmethod
    def get_people_dialogue(namePerson: str) -> dict:
        try:
            #exs.
            if not os.path.isfile(f"api/json/conversations/{namePerson}.json"):
                return {}
                
            with open(f"api/json/conversations/{namePerson}.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                if 'responses' in data and isinstance(data['responses'], list) and len(data['responses']) > 0:
                    #altr.
                    return json.dumps(random.choice(data['responses']))
                else:
                    return {}
        
        except json.JSONDecodeError:
            return {}
        except Exception as e:
            print(f"Erro ao ler o arquivo (api-jsons): {e}")
            return {}
