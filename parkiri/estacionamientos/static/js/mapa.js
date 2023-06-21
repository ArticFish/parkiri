function ubicacion(mapa,dire){
  var mapad= mapa.split("=");
  var comuna = mapad[1].split(",");

  var urlCompleta = mapad[0] + '=' + dire +','+comuna[1] + '=' + mapad[2] + '=' + mapad[3];
  
  return urlCompleta;
}

const div1 = document.getElementById("direccion");
const exampleAttr = div1.getAttribute("name");
var direccion = exampleAttr.replace(/ /g,"+")
var mapaUrl = "http://maps.google.com/maps?q=Manantiales+6017,Santiago&z=15&output=embed";


var iframeElemento = document.getElementById("mi-iframe");
iframeElemento.src = ubicacion(mapaUrl,direccion);