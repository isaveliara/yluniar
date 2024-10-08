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