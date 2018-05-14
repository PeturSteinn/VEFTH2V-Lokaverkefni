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
    <img src="/static/img/{{hotel['folder']}}/{{hotel['border']}}">
  </header>
  <div class="wrapper-index-hotel">

  <div class="box4">
    <form action="/{{hotel['name']}}">
    <div class="stadir">
        <div><label>Check in:</label><input id="1" type="date" name="checkin" required></div>
        <div><label>Check out:</label><input id="2" type="date" name="ckeckout" required></div>
        <div>
          <label>Herbergi:</label>
          <select name="Herbergi">
              <option value="Guset" selected="">Guset(queen)</option>
              <option value="Suites">Suites(queen+bead)</option>
              <option value="Executive">Executive(King+queen)</option>
          </select>
        </div>
        <div>
          <input type="submit" name="Panta">
        </div>
    </div>
     </form>
  </div>

  <div class="wrapper-index">
    <div class="umokkur">
      <div class="myndbox">
        <div class="popup">
          <div class="imgs">
            <img class="slides" src="/static/img/HotelRK/bannerRK.jpg">
            <img class="slides" src="/static/img/HotelAK/bannerAK.jpg">
            <button class="btn" onclick="plusIndex(-1)">&#10094;</button>
            <button class="btn2" onclick="plusIndex(-1)"">&#10095;</button>
          </div>
          <div class="uppls">
    
  </div>
</div>
      </div>
      <div class="text">
        <h1>Um okkur</h1>
        <p>Við opnuðum fyrsta hótleið okkar 2000 í reykjavík, þá vorum við ekki nema með 20 herbergi. Herbergi voru þá bara með eitt rúm og klósetti. 2004 fórum við í nýju bygginguna okkar í reykjavík þar sem við erum núna staðsett. 2006 opnuðum við annað hótel á Akureyri með 10 herbergum, planið var að gá hvernig mundi fara að hafa hótel á Akureyri. 2010 lokuðum við hótelinu í Reykavík út af viðhalningu og oppnuðum að áftur ári eftir þá með 70 herbergum og meira þægindum. Opnuðum nýtt hótel á Selfossi með 35 herbergum árið 2015. Árið 2017 fluttum við hótelið á Akureyri í nýja byggingu sem var byrjuð í framkvæmdum árið 2015. Hótelið er með 45 herbergum og er flottasta hótelið okkar núna</p>      
      </div>  
    </div>

</div>
</div>

<footer>
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
  <div class="footer"><p>Róbert Ingi - Pétur Steinn - Helgi Tuan</p></div>
</footer>
  



 


<script type="text/javascript">
    var index = 1;

    function plusIndex(n){
      index = index + 1;
      showImage(index);
    }

    showImage (1);

    function showImage(n){
      var x = document.getElementsByClassName('slides');
      if (n > x.length) {index = 1};
      if (n < 1) { index = x.length};
      for(i=0;i<x.length;i++)
        {
          x[i].style.display = "none";
        }
        x[index-1].style.display = 'block';
    }
    var checkin = document.getElementsById('1');
    var checkout = document.getElementsById('2');

    function blockcheckout(){
      if (checkin > checkout ){checkout.style.display = "block"}

    }
</script>

</body>