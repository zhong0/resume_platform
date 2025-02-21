let inputContent = document.getElementById('basicIntro_upload_input');
const uploadButton = document.getElementById('basicIntro_upload');
const phoneButton = document.getElementById('basicIntro_phone');
const emailButton = document.getElementById('basicIntro_email');
const githubButton = document.getElementById('basicIntro_github');
const linkedinButton = document.getElementById('basicIntro_linkedin');
let basicInfo = {};


genInitRequestOptions()

function genInitRequestOptions(){
    let account = '{"account": "wz0"}'
    const formData = new FormData();
    formData.append('data', account);
    const requestOptions = {
        method:'POST',
        body: formData
    };

    fetch('/basicInfo/get_basicInfo', requestOptions)
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                console.error('Error:', response.statusText);
                setTimeout(showMessageBox("Get Data Fail"), 1000);
            }
            inputContent.value = "";
        }).then(data => {
            basicInfo = data
        }).catch(error => {
            console.error('Error:', error);
        });
}


uploadButton.addEventListener('click',()=>{
    let inputText = inputContent.value;
    console.log(inputText)
    const formData = new FormData();
    formData.append('data', inputText);

    const requestOptions = {
        method:'POST',
        body: formData
    };

    fetch('/basicInfo/upload_resume', requestOptions)
        .then(response => {
            if (response.ok) {
                closeModal();
                setTimeout(showMessageBox("Upload Successfully"), 1000);
            } else {
                console.error('Error:', response.statusText);
                closeModal();
                setTimeout(showMessageBox("Upload Fail"), 1000);
            }
            inputContent.value = "";
        })
        .catch(error => {
            console.error('Error:', error);
        });
});

phoneButton.addEventListener('click',()=>{
    navigator.clipboard.writeText(basicInfo.phone)
    .then(() => showMessageBox("Phone is copied:\n" + basicInfo.phone))
    .catch(err => console.error("Copied Fail:", err));
});

emailButton.addEventListener('click',()=>{
    navigator.clipboard.writeText(basicInfo.email)
    .then(() => showMessageBox("Email is copied:\n" + basicInfo.phone))
    .catch(err => console.error("Copied Fail:", err));
});

githubButton.addEventListener('click',()=>{
    window.open(basicInfo.github);
});

linkedinButton.addEventListener('click',()=>{
    window.open(basicInfo.linkedin);
});

function showMessageBox(text) {
    let uploadMessage = document.getElementById('basicIntro_upload_message');
    uploadMessage.textContent = text;
    uploadMessage.style.display = 'block';
    setTimeout(() => {
        uploadMessage.style.display = 'none';
    }, 3000);
}

// 打開彈出框
function openModal() {
    document.getElementById("homepage_upload_overlay").style.display = "flex";
}

// 關閉彈出框
function closeModal() {
    document.getElementById("homepage_upload_overlay").style.display = "none";
}
