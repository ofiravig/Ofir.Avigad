
function isEmpty(str) {
    return (!str || str.length === 0 );
}
function MessBox(email,name,msg){
    if(isEmpty(email) || isEmpty(name) || isEmpty(msg)){
        alert("Please fill all fields.");
    }
    else{
    alert("We'll talk soon :)");
    location.href='/';
    }
}


fetch('https://reqres.in/api/users?page=2').then(response => response.json())
.then(responseJSON => createUserList(responseJSON.data)).catch(err =>
console.log(err));

function createUserList(users) {
    console.log(users);
    const curr_main = document.querySelector("main");
    for(let user of users){
        const section = document.createElement("section");
        section.innerHTML = `
        <img src="${user.avatar}" alt="profile">
        <div>
           <span>  ${user.first_name} ${user.last_name} </span>
           <br>
           <a href="mail: ${user.email}">Send Email</a>
        </div>
        `;
        curr_main.appendChild(section);
    }
}