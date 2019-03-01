
window.onload = function() {

  document.getElementById('msgSend').onclick = function(){
    console.log('clicked');

    var textArea = document.getElementById('msgText').value;
    console.log(textArea);

    var paragraph = document.createElement('p');
    var par_text = document.createTextNode(textArea);
    paragraph.append(par_text);
    document.body.appendChild(paragraph);
  };
}
