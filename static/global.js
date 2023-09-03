    document.getElementById('flexSwitchCheckDefault').addEventListener('click', () => {
        if (document.documentElement.getAttribute('data-bs-theme') == 'dark') {
            document.documentElement.setAttribute('data-bs-theme', 'light')
            document.getElementById('darkModeSwitchName').innerText = 'Darkmode';
        } else {
            document.documentElement.setAttribute('data-bs-theme', 'dark')
            document.getElementById('darkModeSwitchName').innerText = 'Lightmode';

        }
    })