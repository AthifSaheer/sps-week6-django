// var loginUnameRequired = document.getElementById("login-uname-required")
// loginUnameRequired.innerHTML = "jfdsklaj"

// var loginUsernameInput = document.getElementById('login-username-input').value;
// console.log(loginUsernameInput)


function usernameFunction() {
    var numbers = /^[0-9]+$/;
    var letters = /^[A-Za-z]+$/;
    var letterNumber = /^[0-9a-zA-Z]+$/;
    var symbol = /^[a-zA-Z0-9.]+@/;
    
    var loginUsernameInput = document.getElementsByName('login-username-input')[0].value;
    var loginUnameRequired = document.getElementById("login-uname-required")
    var loginUnameUnique = document.getElementById("login-uname-unique")
    console.log(loginUnameUnique)

    if (loginUsernameInput.match(letters)) {
        loginUnameRequired.style.visibility = "hidden"
    } else if (!loginUsernameInput.match(letters)) {
        loginUnameRequired.style.visibility = "visible"
    }

    if(!loginUsernameInput.match(numbers)) {
        loginUnameUnique.style.visibility = "hidden"
    }else if(loginUsernameInput.match(numbers) || loginUnameUnique.match(letterNumber)) {
        loginUnameUnique.style.visibility = "visible"
    }
}


// function loginBtn(){
//     var numbers = /^[0-9]+$/;
//     var letters = /^[A-Za-z]+$/;
//     var letterNumber = /^[0-9a-zA-Z]+$/;
//     var symbol = /^[a-zA-Z0-9.]+@/;
    
//     var loginUsernameInput = document.getElementById("login-username-input").value
//     var loginPasswordInput = document.getElementById("login-password-input").value

//     var loginUnameRequired = document.getElementById("login-uname-required")
//     var loginPwordRequired = document.getElementById("login-pword-required")

//     if (loginUsernameInput.match(letterNumber)) {
//         loginUnameRequired.style.visibility = "visible"
//     } else if (!loginUnameRequired.match(letterNumber)) {
//         loginUnameRequired.style.visibility = "visible"
//     }
//     if (loginPasswordInput.match(letterNumber)) {
//         loginPwordRequired.style.visibility = "hidden"
//     } else {
//         loginPwordRequired.style.visibility = "visible"
//     }
// }