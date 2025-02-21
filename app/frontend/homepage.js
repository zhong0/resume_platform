// page scroll
function initFullPage() {
    new fullpage('#fullpage', {
        autoScrolling: true,
        navigation: true,
        navigationPosition: 'right'
    });
}

// basic introduction
function showBasicIntro(){
    fetch('./frontend/basicIntro.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('section1').innerHTML = data;
            let script = document.createElement('script');
            script.src = './frontend/basicIntro.js';
            script.defer = true;
            document.body.appendChild(script);
        })
        .catch(error => console.error('Error loading the page:', error));
}

initFullPage();
showBasicIntro();