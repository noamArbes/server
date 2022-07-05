
  // function markTab(){
  //   for (var i = 0; i < document.links.length; i++) {
  //       if (document.links[i].href === document.URL) {
  //           current = i;
  //       }
  //   }
  //   document.links[current].className = 'current';
  //
  // }
  //


function greet(val){
var hrs = new Date().getHours();
var greet;
var message;
console.log(val);
console.log("hi");

if (hrs < 12){
    greet = 'Good Morning,';
    message ='We will get back to you later today';
}
   
else if (hrs >= 12 && hrs < 17){
    greet = 'Good Afternoon,';
    message ='We will get back to you shortly';
}
    
else if (hrs >= 17 && hrs <= 24){
    greet = 'Good Evening,';
    message ='We will get back to you tommorow morning';  
}
  
if (val == 'lblGreetings'){
    document.getElementById("lblGreetings").innerHTML = greet;

}
else{
    document.getElementById("message").innerHTML = message;
}

}

document.querySelector('#outer-source__form')?.addEventListener('submit',(e)=> {
    e.preventDefault()
    const id = e.target.id.value
    fetch('https://reqres.in/api/users/' + id)
        .then(results => results.json())
        .then(json => {
            const  image = document.querySelector('#outer-source__image1')
             image.classList.remove('invisible')
             image.src = json.data.avatar
        })
        .catch((e) => {
        console.log(e)
        })
})



