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
            file_path = f"api/json/conversations/{namePerson}.json"
            if not os.path.isfile(file_path):
                return {}
            
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if 'responses' in data and isinstance(data['responses'], list) and len(data['responses']) > 0:
                    
                    #distributes the percentages
                    responses = data['responses']
                    choices = []
                    for response in responses:
                        choices.extend([response] * response['percent'])

                    #choice one
                    selected_response = random.choice(choices)
                    return json.dumps(selected_response)
                else:
                    return {}
        
        except json.JSONDecodeError:
            return {}
        except Exception as e:
            print(f"Erro ao ler o arquivo (api-jsons): {e}")
            return {}

