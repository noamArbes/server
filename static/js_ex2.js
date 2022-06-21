
  function markTab(){
    for (var i = 0; i+2 < document.links.length; i++) {
        if (document.links[i].href === document.URL) {
            current = i;
        }
    }
    document.links[current].className = 'current';
       
  }
 


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



