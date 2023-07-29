function handleUserInput() {
    //get text of input box
    var userInput = document.getElementById("user-input").value;

    //get text of chat history
    var chatHistory = document.getElementById("chat-history").value;

    //append inputVal to value of text box
    document.getElementById("chat-history").value = chatHistory + "\n" + userInput;
    document.getElementById("user-input").value = ""

    // alert(inputVal)


    let csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value

    let user_input = {
        input: userInput,
        csrfmiddlewaretoken: csrfToken
    }


    let post = JSON.stringify(user_input)
    const url = "/ai_handle_input"
    let xhr = new XMLHttpRequest()
    xhr.open('POST', url, true)
    xhr.setRequestHeader('Content-type', 'application/json; charset=UTF-8')
    xhr.send(post);
    xhr.onload = function () {
        if (xhr.status === 201) {
            console.log("Post successfully created!")
        }
    }


}