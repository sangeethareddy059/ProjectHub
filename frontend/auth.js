

const authModal =
document.getElementById(
    "authModal"
);

const registerForm =
document.getElementById(
    "registerForm"
);

const loginForm =
document.getElementById(
    "loginForm"
);

const forgotForm =
document.getElementById(
    "forgotForm"
);


function openRegister(){

    authModal.style.display =
    "flex";

    registerForm.style.display =
    "flex";

    loginForm.style.display =
    "none";

    forgotForm.style.display =
    "none";

}


function openLogin(){

    authModal.style.display =
    "flex";

    loginForm.style.display =
    "flex";

    registerForm.style.display =
    "none";

    forgotForm.style.display =
    "none";

}


function openForgot(){

    authModal.style.display =
    "flex";

    forgotForm.style.display =
    "flex";

    loginForm.style.display =
    "none";

    registerForm.style.display =
    "none";

}


async function registerUser(e){

    e.preventDefault();

    const name =
    document.getElementById(
        "registerName"
    ).value;

    const email =
    document.getElementById(
        "registerEmail"
    ).value;

    const password =
    document.getElementById(
        "registerPassword"
    ).value;


    const response = await fetch(

        "http://127.0.0.1:8000/api/register/",

        {

            method:"POST",

            headers:{
                "Content-Type":
                "application/json"
            },

            body:JSON.stringify({

                name,
                email,
                password

            })

        }

    );


    const result =
    await response.json();


    if(result.error){

        alert(result.error);

    }

    else{

        alert(result.message);

        openLogin();

    }

}


async function loginUser(e){

    e.preventDefault();

    const email =
    document.getElementById(
        "loginEmail"
    ).value;

    const password =
    document.getElementById(
        "loginPassword"
    ).value;


    const response = await fetch(

        "http://127.0.0.1:8000/api/login/",

        {

            method:"POST",

            headers:{
                "Content-Type":
                "application/json"
            },

            body:JSON.stringify({

                email,
                password

            })

        }

    );


    const result =
    await response.json();


    if(result.error){

        alert(result.error);

    }

    else{

        alert(result.message);

        localStorage.setItem(
            "loggedIn",
            "true"
        );

        localStorage.setItem(
            "username",
            result.username
        );


        const savedProjectId =

        localStorage.getItem(
            "projectId"
        );


        if(savedProjectId){

            localStorage.removeItem(
                "projectId"
            );

            window.location.href =

            `project-details.html?id=${savedProjectId}`;

        }

        else{

            window.location.reload();

        }

    }

}


async function forgotPassword(e){

    e.preventDefault();

    const button =

    document.getElementById(
        "changePasswordBtn"
    );

    button.innerText =
    "Updating...";

    button.disabled = true;


    const email =

    document.getElementById(
        "forgotEmail"
    ).value;


    const newPassword =

    document.getElementById(
        "forgotNewPassword"
    ).value;


    try{

        const response = await fetch(

            "http://127.0.0.1:8000/api/forgot-password/",

            {

                method:"POST",

                headers:{
                    "Content-Type":
                    "application/json"
                },

                body:JSON.stringify({

                    email,
                    new_password:newPassword

                })

            }

        );


        const result =
        await response.json();


        if(result.error){

            alert(result.error);

        }

        else{

            alert(
                "Password Changed Successfully"
            );

            openLogin();

        }

    }

    catch(error){

        alert(
            "Something went wrong"
        );

    }


    button.innerText =
    "Change Password";

    button.disabled = false;

}


function logout(){

    localStorage.removeItem(
        "loggedIn"
    );

    localStorage.removeItem(
        "username"
    );

    alert(
        "Logout Successful"
    );


    window.location.reload();

}



function toggleMenu(){

    const menu =
    document.getElementById(
        "profileMenu"
    );

    if(!menu) return;


    if(menu.style.display === "block"){

        menu.style.display =
        "none";

    }

    else{

        menu.style.display =
        "block";

    }

}



window.onload = function(){

    const loggedIn =
    localStorage.getItem(
        "loggedIn"
    );

    const username =
    localStorage.getItem(
        "username"
    );

    const profile =
    document.getElementById(
        "userProfile"
    );

    const profileUsername =
    document.getElementById(
        "profileUsername"
    );


    if(profile){

        if(loggedIn === "true"){

            profile.style.display =
            "block";

            if(profileUsername){

                profileUsername.innerText =
                username;

            }

        }

        else{

            profile.style.display =
            "none";

        }

    }

}



function openChat(){

    const chatBox =
    document.getElementById(
        "chatBox"
    );

    if(chatBox){

        chatBox.style.display =
        "flex";

    }

}



function closeChat(){

    const chatBox =
    document.getElementById(
        "chatBox"
    );

    if(chatBox){

        chatBox.style.display =
        "none";

    }

}



async function sendMessage(){

    const input =

    document.getElementById(
        "chatInput"
    );

    const message =
    input.value;

    const username =

    localStorage.getItem(
        "username"
    );


    if(message.trim() === ""){

        return;

    }


    const response = await fetch(

        "http://127.0.0.1:8000/api/send-message/",

        {

            method:"POST",

            headers:{
                "Content-Type":
                "application/json"
            },

            body:JSON.stringify({

                username,
                message

            })

        }

    );


    const result =
    await response.json();


    alert(result.message);

    input.value = "";

}