function goToAiChat() {
    window.location.href='/ai_chat';
}
function goToConversationalAiChat(){
    window.location.href='/conversational_ai_chat';
}
function enableDarkMode()   {
    const htmlTag = document.getElementsByTagName("html")[0];
    htmlTag.setAttribute("data-bs-theme", "dark");
}
function enableLightMode() {
    const htmlTag = document.getElementsByTagName("html")[0];
    htmlTag.setAttribute("data-bs-theme", "light");
}