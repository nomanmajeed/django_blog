


console.log("ss")
function login(){
    var username = document.getElementById('loginUsername').value
    var password = document.getElementById('loginPassword').value
    var csrf = document.getElementById('csrf').value

    if(username == '' && password == ''){
        alert('You must enter both')
    }

    var data = {
        'username' : username,
        'password' : password
    }

    fetch('/api/login/' , {
        method : 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrf,
        },
       
        body : JSON.stringify(data)
    }).then(result => {
        result.json()
        console.log("here 1: ", response)
    }).then(response => {
        console.log("here 2: ", response)
        if(response.status == 200){
            window.location.href = '/'
        }
        else{
            alert(response.message)
        }

    })

}


function register(){
    var username = document.getElementById('loginUsername').value
    var password = document.getElementById('loginPassword').value
    var csrf = document.getElementById('csrf').value

    if(username == '' && password == ''){
        alert('You must enter both')
    }

    var data = {
        'username' : username,
        'password' : password
    }

    fetch('/api/register/' , {
        method : 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrf,
        },
       
        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
        console.log(response)
        if(response.status == 200){
          
        }
        else{
            alert(response.message)
        }

    })

}