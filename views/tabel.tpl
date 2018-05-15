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
      <div class="box2"><ul><li></form><a href="/bokunn">Sjá bókun</a></li><li><a href="/starfsmenn">Starfsfólk</a></li><li><a href="#umokkuer">Um okkur</a></li><li><a href="/Hotel/akureyri">Akureyri</a></li><li><a href="/Hotel/selfoss">Selfoss</a></li><li><a href="/Hotel/reykjavik">Reykavík</a></li><li><a href="/">Forsíða</a></li></ul></div>
      <div class="box3"><h1>Velkominn á síðuna hjá Hraun Hótel</h1><p class="text">Við erum með 3 hótel sem eru staðsett á Íslandi. 70 herbergja í Reykjavík, 45 herbergja á Akureyri, 35 herbergja á Selfossi.</p><p class="text2">Það er hægt að pnata ferðir á Hótelunum, boði eru reyðtúrar, jökklaferðir, hvalaleiðangrar, fjöllgöngur og mikklu fleira.</p></div>
    </div>
  <img src="/static/img/akureyri/akureyri.jpg">
  </header>
  
  <div class="wrapper-tabel">
    % for x in orders:
      <button class="accordion">{{x['hotel']}}, {{x['checkin']}}-{{x['checkout']}}</button>
      <div class="panel">
        <p><table class="minimalistBlack" style="height: 88px;" width="384">
          <thead>
          <tr>
          <th>Herbergi</th>
          <th>Herbergisnúmer</th>
          <th>Herbergistegund</th>
          <th>Verðnótt</th>
          <th>Lengdgistingar</th>
          <th>Heldaverð herbergis</th>
          </tr>
          </thead>
          <tfoot>
          <tr>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td>Heildaverð pöntunar</td>
          <td>{{x['orderprice']}}</td>
          </tr>
          </tfoot>
          <tbody>
            % teljari = 1
            % for y in x['herbergi']:
              <tr>
              <td>herbergi {{teljari}}</td>
              <td>{{y['nuber']}}</td>
              <td>{{y['type']}}</td>
              <td>{{y['price']}}</td>
              <td>{{y['days']}}</td>
              <td>{{y['totalprice']}}</td>
              </tr>
              % teljari += 1
            % end
          </tbody>
          </table>
        </p>
      </div>
  % end
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
</script>
