Using the `/api/calc` route:
- This route returns the result of the equation as an image. But don’t get too excited, it’s working about as well as a square ball.

- **Quadratic equations**: Use the form `ax² + bx + c = 0`, where `a`, `b`, and `c` are constants.
  - Example: `2x² + 3x + 1 = 0`
  
- **Linear equations**: If there's no `x²` term, it becomes a linear equation.
  - Example: `3x + 9 = 0`
  
- **Special cases**:
  - Missing linear term: `x² - 16 = 0`
  - Perfect square trinomial: `x² + 4x + 4 = 0`
  - Zero coefficient for quadratic: `0x² + 5x + 10 = 0` (treated as linear)

- **Complex roots**: If the discriminant is negative (e.g., `x² + 1 = 0`), expect complex roots.
  
- **Invalid equations**: Equations like `4 = 0` won't work as there's no variable `x`.


Using `api/people/{person}` and `api/people/{person}/says` routes:

- These routes are just jokes, where the first one returns all phrases of the person, and the second one an already chosen phrase.
  - Example: `api/people/preceptor`
    returns all phrases.
  - Example: `api/people/preceptor/says`

    ```json
    {
        "text": "eu ri",
        "percent": 7
    }
    ```

Using `/api/quiz/theme/<string:theme>` route:

- This route returns the full json of the theme
  - Example: `/api/quiz/theme/doors`
  returns the full json of the theme "doors". (the answer is a regex)

  format:
  ```json
  {
    "quiz_info": {
        "requires" : "user",
        "version" : "1.1",
        "questionsLimite": -1, //infinite
        "revealAnswerOnFail": true,
        "attempts": -1, //infinite
        "pointsForUserWin": -1, //infinite
        "rate": 30,
        "rateVariance": 5 //variance of rate in seconds
    },
    "questions": [
        {
            "index" : 1,  "worth": 3,"response_file" : null,
            "build": {
                "title": "My Theme Q1",
                "description": "string",
                "color": "#FF5733",  "file" : null,  "footer": "1 valid answer",
            },
            "response": "string",
            "answers": [
                "^uses regex response$" //uses regex
            ]
        }
    ]
  }
  ```

  - Also, you can use the `/api/quiz/question/<string:theme>` route to get a specific question.
  Like this:
  ```json
  {
  "response": {
    "answers": [
      "^yes$"
    ],
    "build": {
      "color": "#FF5733",
      "description": "yes or no?",
      "file": null,
      "footer": "1 valid answer",
      "title": "Theme"
    },
    "index": 1,
    "response": "Yes! This is correct",
    "response_file": null,
    "worth": 3
  },
  "status": "success"
  }
  ```