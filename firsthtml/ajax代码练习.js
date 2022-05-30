
function loadImg(){
  var xmlHttp;
  if(window.XMLHttpRequest){
    xmlHttp = new XMLHttpRequest;}
  else{
  xmlHttp = new ActiveXObject("Microsoft.XMLHttp");
      }
  xmlHttp.onreadystatechange=function(){
     if(xmlHttp.readyState == 4 && xmlHttp.status== 200){
             document.getElementById("da").src="黑丝小短裙.jpg";
         }
       }
     xmlHttp.open("GET","黑丝小短裙.jpg",true);
     xmlHttp.send();
     window.alert("那层层叠叠的鲜嫩瓣上水渍闪烁，更为那朵直径不足两寸的秘之花增加了几许诱惑和妖艳");
    loadImg();
}
