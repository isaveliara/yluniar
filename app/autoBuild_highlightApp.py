import re
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Token:
    type: str
    value: str
    pos: Tuple[int, int]  # (linha, coluna)

class NPTTokenizer:
    def __init__(self):
        # Ordem das regras de precedência para o highlight
        self.token_specs = [
            ('comment', r'--.*'),                 # Comentários
            ('literal', r"s'[^']*'|c'.?'"),       # Strings/chars
            ('placeholder', r'&\{\w+\}'),         # Placeholders
            ('variable', r'\$\{\w+\}'),           # Variáveis
            ('keyword', r'&\w+|#script\b'),       # Palavras-chave (agora inclui #script)
            #('keyword2', r'include|set'),
            ('property', r'::\s*\w+'),            # Propriedades
            ('type', r'(Str|Int|Float|Error|Nil|List|Dict|User|Char)\b'),  # Tipos
            ('number', r'\b\d+\.?\d*\b'),         # Números
            ('operator', r'->|::|>=|<=|==|~=|\+\+|\-\-|&&|\|\||[+\-*/?!;,#|><=~]'),  # Operadores
            ('bracket', r'[][(){}]'),             # Brackets
            ('dot', r'\.(?=\s|$)'),               # Pontos finais
            ('identifier', r'[a-zA-Z_]\w*'),      # Identificadores
            ('remaining', r'.'),                  # Caracteres restantes
        ]

        self.regex = re.compile(
            '|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.token_specs),
            flags=re.DOTALL | re.MULTILINE
        )

    def tokenize(self, code: str) -> List[Token]:
        """Transforma o código NPT em tokens para formatação."""
        tokens = []
        line_num = 1
        line_start = 0

        for mo in self.regex.finditer(code):
            kind = mo.lastgroup
            value = mo.group()
            column = mo.start() - line_start

            if '\n' in value:
                line_num += value.count('\n')
                line_start = mo.end() - (len(value) - value.rfind('\n') - 1)

            tokens.append(Token(kind, value, (line_num, column)))

        return tokens

def highlight_npt(code: str) -> str:
    """Transforma tokens em HTML formatado para highlight."""
    tokenizer = NPTTokenizer()
    tokens = tokenizer.tokenize(code)

    html = []
    for token in tokens:
        html.append(f'<span class="{token.type}">{token.value}</span>')
    
    return f"""
    <div class="codeblock-npt">
        <div class="npt-header">Нпт</div>
        <pre class="code-content">{''.join(html)}</pre>
    </div>
    """

@app.route("/")
def index():
    sample_code = """~Str set var s'Hello' + s' World' .
~include std .

#script .
nout() -> ${var}
&if ( &true == &false ) &do{
    &forget
}"""
    highlighted_code = highlight_npt(sample_code)
    return render_template("nptEditor.html", codeblock=highlighted_code)

@app.route("/highlight", methods=["POST"])
def highlight_api():
    """API para processar código e retornar HTML formatado."""
    data = request.get_json()
    code = data.get("code", "")
    highlighted_code = highlight_npt(code)
    return jsonify({"highlighted_code": highlighted_code})

if __name__ == "__main__":
    app.run(debug=True)
