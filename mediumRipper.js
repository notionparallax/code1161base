a = document.querySelectorAll("[data-username]")
b = [];

function pullUserName(x){
  b.push( x.getAttribute("data-username"));
}

a.forEach(pullUserName) //I don't like this, I'd rather use a map
b.forEach(function(x){console.log(x)})
