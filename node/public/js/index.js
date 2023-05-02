const titles = []
var idCard = 0;

function getTexts() {
    $(".modal-info-loader").show("slow");

    $.get('/getInfo', function (res) {
        console.log("res ", res);

        if(res.status == 200) {
            var text = res.text;
            
            if (text.includes('assunto')) {
                var words = text.split(" ");
                
                // assunto existe
                if(titles.indexOf(words[1]) !== -1) {
                    populateCurrentCard(words, text);
                } 
                
                // assunto nao existe
                else {
                    createNewCard(words)
                }

            } else {
                if (titles.length == 0) {
                    toastr["error"]("Primeiro crie um assunto");
                } else {
                    populatePreviousCard(text)
                }
            }

            $(".modal-info-loader").hide("slow");

        } else {
            $(".modal-info-loader").hide("slow");
            toastr["error"]("Ocorreu um erro ao capturar som e texto");
        }

    })
}

function createNewCard(words) {
    idCard += 1;

    toastr["success"]("Novo assunto criado");

    titles.push(words[1]);

    // Cria o novo card
    var newCard = document.createElement("div");
    newCard.classList.add("card");
    newCard.classList.add(words[1]);
    newCard.id = idCard

    // Cria o titulo
    var newTitle = document.createElement("span");
    newTitle.classList.add("title-card");

    // Adiciona o texto ao titulo
    newTitle.textContent = 'Assunto: ' + words[1];

    // Adiciona o titulo ao card
    newCard.appendChild(newTitle);

    // Adiciona o novo card ao painel principal
    var containerDiv = document.getElementById("card-content");
    containerDiv.appendChild(newCard);
}

function populateCurrentCard(words, text) {
    let curretCard = document.querySelector("."+words[1]);
    idCard = curretCard.id;

    const justText = text.split(words[1])

    // Cria o texto
    var newText = document.createElement("span");
    newText.classList.add("title-content");

    // Adiciona o texto ao titulo
    newText.textContent = justText[1];

    // Adiciona o titulo ao card
    curretCard.appendChild(newText);
}

function populatePreviousCard(text) {
    let curretCard = document.getElementById(idCard);
                    
    // Cria o texto
    var newText = document.createElement("span");
    newText.classList.add("title-content");

    // Adiciona o texto ao titulo
    newText.textContent = text;

    // Adiciona o titulo ao card
    curretCard.appendChild(newText);
}

function closeModalInfo() {
    $(".modal-info").hide("slow");
}