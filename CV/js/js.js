
function isEmpty(str) {
    return (!str || str.length === 0 );
}
function MessBox(email,name,msg){
    if(isEmpty(email) || isEmpty(name) || isEmpty(msg)){
        alert("Please fill all fields.");
    }
    else{
    alert("We'll talk soon :)");
    location.href='../html/home.html';
    }
}
