import json, random, os

class PeopleService:
    @staticmethod
    def get_people(namePerson: str) -> dict:
        try:
            file_path = f"api/json/conversations/{namePerson}.json"
            if not os.path.isfile(file_path):
                return {"status": "error", "response": f"Pessoa '{namePerson}' não encontrada."}
                
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return {"status": "success", "response": data}
        
        except json.JSONDecodeError:
            return {"status": "error", "response": "Erro ao decodificar JSON."}
        except Exception as e:
            return {"status": "error", "response": f"Erro ao ler o arquivo: {e}"}
        
    @staticmethod
    def get_people_dialogue(namePerson: str) -> dict:
        try:
            file_path = f"api/json/conversations/{namePerson}.json"
            if not os.path.isfile(file_path):
                return {"status": "error", "response": f"Pessoa '{namePerson}' não encontrada."}
            
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if 'responses' in data and isinstance(data['responses'], list) and len(data['responses']) > 0:
                    responses = data['responses']
                    
                    # Distribuir as porcentagens
                    choices = []
                    for response in responses:
                        choices.extend([response] * response['percent'])
                    
                    # Escolher uma resposta aleatória
                    selected_response = random.choice(choices)
                    return {"status": "success", "response": selected_response}
                else:
                    return {"status": "error", "response": "Nenhuma resposta encontrada."}
        
        except json.JSONDecodeError:
            return {"status": "error", "response": "Erro ao decodificar JSON."}
        except Exception as e:
            return {"status": "error", "response": f"Erro ao ler o arquivo: {e}"}



class QuizService:
    @staticmethod
    def load_json_data(filename):
        file_path = f"./api/json/quiz/new/{filename}.json"
        if not os.path.exists(file_path):
            return {"status": "error", "response": f"Arquivo '{filename}' não encontrado."}
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return {"status": "success", "response": data}
        except Exception as e:
            return {"status": "error", "response": f"Erro ao ler o arquivo: {e}"}
    
    @staticmethod
    def save_json_data(filename: str, data: json):
        file_path = f"./api/json/quiz/{filename}.json"
        if not os.path.exists(file_path):
            return {"status": "error", "response": f"Arquivo '{filename}' não encontrado."}
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
                return {"status": "success", "response": data}
        except Exception as e:
            return {"status": "error", "response": f"Erro ao salvar o arquivo: {e}"}
    

    @staticmethod
    def get_question_data(filename: str):
        quiz_data = QuizService.load_json_data(filename)
        if quiz_data['status'] == "error":
            return quiz_data['response']
        
        return {"status": "success", "response": quiz_data["response"]}
    
    @staticmethod
    def get_individual_question(filename: str):
        quiz_data = QuizService.load_json_data(filename)
        if quiz_data['status'] == "error":
            return quiz_data['response']
        
        questions = quiz_data['response'].get('questions', [])
        if not questions:
            return f"Nenhuma pergunta encontrada para o tema '{filename}'."
        
        random_question = random.choice(questions)
        return {"status": "success", "response": random_question}

class ListenersService:
    @staticmethod
    def returnATestListener(serverid: int, typelisten: str):
        file_path = f"./api/json/heartbeats/{typelisten}.json"
        if not os.path.exists(file_path):
            return {"status": "error", "response": f"Listener '{typelisten}' não encontrado."}
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return {"status": "success", "response": data}
        except Exception as e:
            return {"status": "error", "response": f"Erro ao ler o listener: {e}"}