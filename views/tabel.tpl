<!DOCTYPE html>
<html>

<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta charset="utf-8">
  <title>HraunHotel</title>
  <link rel="stylesheet" href="/static/css/main.css">
  <link rel="stylesheet" href="/static/css/normalize.css">
  <link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet">
</head>
<body>
  <header>
    <div class="navbar">
      <div class="box"><img src="/static/img/mynd.png" style="width: 82px;"></div>
      <div class="box2"><ul><li><a href="/bokun">Sjá bókun</a></li><li><a href="/starfsmenn">Starfsfólk</a></li><li><a href="#umokkuer">Um okkur</a></li><li><a href="/Hotel/Akureyri">Akureyri</a></li><li><a href="/Hotel/Selfoss">Selfoss</a></li><li><a href="/Hotel/Reykavik">Reykavík</a></li></ul></div>
      <div class="box3"><h1>Velkominn á síðuna hjá Hraun Hótel</h1><p class="text">Við erum með 3 hótel sem eru staðsett á Íslandi. 70 herbergja í Reykjavík, 45 herbergja á Akureyri, 35 herbergja á Selfossi.</p><p class="text2">Það er hægt að pnata ferðir á Hótelunum, boði eru reyðtúrar, jökklaferðir, hvalaleiðangrar, fjöllgöngur og mikklu fleira.</p></div>
    </div>
    <img src="/static/img/HotelAK/bannerAK.jpg">
  </header>
  % if (villa):
      <div class="alert">
        <span class="closebtn">&times;</span>  
        <strong>Villa!&nbsp;</strong>{{villa}}
      </div>
  % end
  % if(user):
   <div class="wrapper-tabel">
    <button class="accordion">Bókanir frammundan</button>
    <div class="panel">
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
    </div>
    <button class="accordion">Allar bókanir</button>
    <div class="panel">
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
    </div>
</div>

  <div class="wrapper">
    <div class="box"><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    </p></div>
    <div class="box"><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    </p></div>
    <div class="box"><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    </p></div>
  </div>
  % else:
  <div class="wrapper-tabell">
    <div class="login" id=id01>
      <div class="contaner">
        <form action="/bokun" method="post">
          <div class="fyrstidalkur">
            <div class="mynd"><img src="/static/img/mynd.png"></div>
          </div>
          <div class="seinni">
          <input type="text" placeholder="Notandanafn:" name="user" required>
          <input type="password" placeholder="Lykilorð:" name="password" required>
            <input type="submit" name="submit" value="Skrá sig inn">
        </div>
        </form>
      </div>
    </div>
  </div>
<footer>
<div class="footer"><p>Róbert Ingi - Pétur Steinn - Helgi Tuan</p></div>
</footer>
</body>
</html>
<script>
var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.maxHeight){
      panel.style.maxHeight = null;
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
    } 
  });
}

var close = document.getElementsByClassName("closebtn");
var i;

for (i = 0; i < close.length; i++) {
    close[i].onclick = function(){

        var div = this.parentElement;

        div.style.opacity = "0";


        setTimeout(function(){ div.style.display = "none"; }, 600);
    }
}
</script>