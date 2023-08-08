function handleUserInput() {
    //get text of input box
    var userInput = document.getElementById("user-input").value;
    if (userInput===""){
        return
    }
    //get text of chat history
    var chatHistory = document.getElementById("chat-history").value;

    //append inputVal to value of text box
    if (chatHistory===""){
        document.getElementById("chat-history").value = userInput;
    }
    else {
        document.getElementById("chat-history").value = chatHistory + "\n" + userInput;
    }
    document.getElementById("user-input").value = ""

    // alert(inputVal)


    let csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value

    let user_input = {
        input: userInput
    }


    let post = JSON.stringify(user_input)
    const url = "/ai_handle_input"
    let xhr = new XMLHttpRequest()
    xhr.open('POST', url, true)
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded')
    xhr.setRequestHeader('X-CSRFToken', csrfToken)
    xhr.send(post);
    xhr.onload = function () {
        if (xhr.status === 201) {
            var newChatHistory = document.getElementById("chat-history").value;
            document.getElementById("chat-history").value = newChatHistory + "\n" +xhr.responseText
            console.log(xhr.responseText)
        }
    }
}

document.getElementById("user-input")
    .addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode === 13) {
        handleUserInput();
    }
});