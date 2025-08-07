function limpar(){
    expressao = ""
    visor.value = ""
}

function apagar(){
    if (" ".includes(expressao[expressao.length - 1])){
        expressao = expressao.slice(0, -3)
    }
    else{
        expressao = expressao.slice(0, -1)
    }
    visor.value = expressao
}

function tokenize(expressao){
    let tokens = []
    let num_atual = ""


    for(let char of expressao){
        if ("0123456789.".includes(char)){
            num_atual += char
        }
        else if ("+-/*".includes(char)){
            if(char === "-" && expressao.indexOf(char) === 0){
                num_atual += "-"
            }
            else{
                if (num_atual !== ""){
                tokens.push(num_atual)
                num_atual = ""
            }
                tokens.push(char)
            }
        }
    }
    if (num_atual !== "") {
        tokens.push(num_atual)
    }

    return tokens
}

function calcular(tokens){
    let resultado = 0
    
    // resolve por prioridade multiplicação e divisão
    for(i = 0; i < tokens.length; i++){
        
        resultado = 0

        if (tokens[i] === "*" || tokens[i] === "/"){
            let num_anterior = parseFloat(tokens[i - 1])
            let num_proximo = parseFloat(tokens[i + 1])

            if(tokens[i] === "*"){
                resultado = num_anterior * num_proximo
                //retira do array o num_anterior, o num_proximo e o operador, e substitui pelo resultado
                tokens.splice(i - 1, 3, resultado) 
                i-=2
            }

            else{
                resultado = num_anterior / num_proximo
                //retira do array o num_anterior, o num_proximo e o operador, e substitui pelo resultado
                tokens.splice(i - 1, 3, resultado)
                i-=2
            }
        }
    }

    // resolve as operações restantes(soma e subtração)

    for(x = 0; x < tokens.length; x++){
        if(tokens[x] === "+"){
            let num_antes = parseFloat(tokens[x - 1])
            let num_depois = parseFloat(tokens[x + 1])

            let r = num_antes + num_depois
            tokens.splice(x - 1, 3, r)
            x -= 2
        }

        if(tokens[x] === "-"){
            let num_antes = parseFloat(tokens[x - 1])
            let num_depois = parseFloat(tokens[x + 1])

            let r = num_antes - num_depois
            tokens.splice(x - 1, 3, r)
            x -= 2
        }
    }

    // função para retornar o resultado final (soma de todos os números do array)
    let soma = 0
    tokens.forEach(num =>{
        soma += num
    })

    expressao = soma.toString()
    return soma
}


function resultado(){
    let x = tokenize(expressao)
    let resultado = calcular(x)
    visor.value = resultado

}

let expressao = ""

const visor = document.getElementById("visor")
const botoes = document.querySelectorAll("button[data-valor]")

// armazena o valor do botão clicado na variavel expressao, que é uma string
botoes.forEach(botao =>{
    botao.addEventListener("click", () =>{
        const valor = botao.getAttribute("data-valor") // acessa o valor do botão atribuido no html
        if("+-*/".includes(valor)){
            if(valor === "-"){
                if(expressao === ""){
                    expressao += "-"
                }

                else{
                    expressao += " - "
                }
            }
            else{
            expressao += ` ${valor} `
            }
            
        }
        else{
            expressao += valor
        }
        visor.value = expressao // usa o .value para passar a a var expressao para o visor e ficar visivel na pagina
    })
})


// botão de limpar
document.getElementById("limpar").addEventListener("click", limpar)

// botão de apagar
document.getElementById("apagar").addEventListener("click", apagar)

// para calcular
document.getElementById("igual").addEventListener("click", resultado)



