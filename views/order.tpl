<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta charset="utf-8">
  <title>HraunHotel - order</title>
  <link rel="stylesheet" href="/static/css/main.css">
  <link rel="stylesheet" href="/static/css/normalize.css">
  <link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet">
</head>
<body>
	<header>
     <div class="navbar">
      <div class="box"><img src="/static/img/mynd.png" style="width: 82px;"></div>
      <div class="box2"><ul><li><a href="/bokunn">Sjá bókun</a></li><li><a href="/starfsmenn">Starfsfólk</a></li><li><a href="#umokkuer">Um okkur</a></li><li><a href="/Hotel/akureyri">Akureyri</a></li><li><a href="/Hotel/selfoss">Selfoss</a></li><li><a href="/Hotel/reykjavik">Reykavík</a></li><li><a href="/">Forsíða</a></li></ul></div>
    </div>
      
  </header>

  <div class="wrapper-oreder">
  	<div class="login" id=id01>
  		<div class="contaner">
	  		<form action="/login" method="post">
	  			<div class="fyrstidalkur">
	  				<span onclick="document.getElementById('id01').style.display='none'" class="close" title="Close Modal">&times;</span>
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
  	<div class="signing" id=id02>
  		<div class="contaner">
	  		<form action="/signup" method="post">
	  			<div class="fyrstidalkur">
	  				<span onclick="document.getElementById('id02').style.display='none'" class="close" title="Close Modal">&times;</span>
	  				<h1>Búa til notanda</h1>
	  			</div>
	  			<div class="seinni">
	  				<div>	
						<input class="input" type="text" placeholder="Notandanafn:" name="user" required pattern="[a-zA-Z]{,20}" title="einginn tölustafur og má ekki vera lengar en 20 stafir">
						<input class="input" type="password" placeholder="Lykilorð:" name="password" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Þarf að innihalda allavega einn tölustaf og einn stáran staf og einn lítinnstaf, og þarf að vera meira en 8 á stafir/tolur á lengd" required>
						<input  class="input" type="text" placeholder="Kennitala:" name="ssn" required pattern="[0-9]{10}" title="Bara 10 tölustaf">
						<input class="input" type="text" placeholder="Fornafn:" name="fname" required>
						<input class="input" type="text" placeholder="Eftirnafn:" name="lname" required>
						<input class="input" type="mail" placeholder="Netfang:" name="mail" pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$" required>
						<input class="input" type="text" placeholder="Sími:" name="phone" pattern="\d{3}(?:[\-\s]?)\d{4}" title="Sláðu inn 7 tölustafi" required>
					</div>
					<div>
						<input class="input" type="text" placeholder="Land:" name="CountryName" required>
						<input class="input" type="text" placeholder="Borg/Bær:" name="CityName" required>
						<input class="input" type="text" placeholder="Götuheiti:" name="StreetName" required>
						<input class="input" type="text" placeholder="Póstnúmer:" placeholder="[0-9],{3}" name="Zip" required>
						<input class="input" type="text" placeholder="Húsnúmer:" name="BuildingNum" required>
						<input class="input" type="text" placeholder="Herbergisnumer / fyrir blokk:" name="ApartNum" >
						<input style="border: 1px solid #ccc; border-radius: 4px;" type="submit" name="submit" value="Búa til notanda">

					</div>

				</div>
  			</form>
  		</div>
  	</div>
  	% if (villa):
	  	<div class="alert">
	  		<span class="closebtn">&times;</span>  
	  		<strong>Villa!&nbsp;</strong>{{villa}}
	  	</div>
	% end
  	<div class="order">
  		<h1>Order</h1>
  			<div class="dalkar">
		  		<div class="fyrsti">
		  			<div class="textbox">
		  				<p>Þú verður að eiga aðgang til að panta herbergi. Ef þú ert ekki með aðgang búður þér til með því að ýta á takkan fyrir neðan(Búa til aðgang). Ef þú átt notanda nú þegar ýttu á hinn takkan.</p>
		  				<div class="takkar">
		  					<button onclick="document.getElementById('id02').style.display='block'">Búa til aðgang</button>
		  					<button onclick="document.getElementById('id01').style.display='block'">Skrá sig inn</button>
		  				</div>
		  			</div>
	  				<form action="/checkorder" method='post'>
			  			<div>

			  			<label>Hotel:</label>
			  			
			  			<select name="hotel">
			  			% if herbergi_uppl['Hotel'] == 'Reykavik': 
			  			  <option  selected value="1">Hraun Hotel Reykjavík</option>
			  			% else:
			  				<option value="1">Hraun Hotel Reykjavík</option>
			  			% end

			  			% if herbergi_uppl['Hotel'] == 'Akureyri': 
			  			  <option selected value="2">Hraun Hotel Akureyri</option>
			  			% else:
			  				<option value="2">Hraun Hotel Akureyri</option>
			  			% end

			  			% if herbergi_uppl['Hotel'] == 'Selfoss': 
			  			  <option  selected value="3">Hraun Hotel Selfoss</option>
			  			% else:
			  				<option value="3">Hraun Hotel Selfoss</option>
			  			% end
			  			</select>
			  			</div>
			  			<p></p>
			  			<div>
			  			<select name="Guset">
			  			  % if 	herbergi_uppl['herbergi'] == 'Guset':
				  			  % for x in range(10):
				  			  % if x+1 == 1:
				  			  	<option selected value="{{x+1}}">{{x+1}} Herbegi</option>
				  			  % else:
				  			  	<option value="{{x+1}}">{{x+1}} Herbegi</option>
				  			  % end
				  			  % end
				  		  % else:
				  		   % for x in range(10):
				  			  	<option  value="{{x}}">{{x}} Herbegi</option>
				  			  % end
				  		  % end
						</select>
			  			<p>Guset(queen):</p>
			  			</div>
			  			<div>
			  			<select name="Suites">
			  			  % if 	herbergi_uppl['herbergi'] == 'Suites':
				  			 % for x in range(10):
				  			  % if x+1 == 1:
				  			  	<option selected value="{{x+1}}">{{x+1}} Herbegi</option>
				  			  % else:
				  			  	<option value="{{x+1}}">{{x+1}} Herbegi</option>
				  			  % end
				  			  % end
				  		  % else:
				  		   % for x in range(10):
				  			  	<option  value="{{x}}">{{x}} Herbegi</option>
				  			  % end
				  		  % end
						</select>

			  			<p>Suites(queen+bead):</p>
			  			</div>
			  			<div>
			  			<select name="Executive">
			  			  % if 	herbergi_uppl['herbergi'] == 'Executive':
				  			 % for x in range(10):
				  			  % if x+1 == 1:
				  			  	<option selected value="{{x+1}}">{{x+1}} Herbegi</option>
				  			  % else:
				  			  	<option value="{{x+1}}">{{x+1}} Herbegi</option>
				  			  % end
				  			  % end
				  		  % else:
				  		   % for x in range(10):
				  			  	<option value="{{x}}">{{x}} Herbegi</option>
				  			  % end
				  		  % end
						</select>

			  			<p>Executive(King+queen):</p>
			  			</div>
		  			
			  	</div>
			  	<div class="eftir">
			  		% if ifuser:
			  			<label>Notandanafn:</label>
				  		<input type="text" name="user" value="{{user['name']}}" readonly required>
				  		<label>Fornafn:</label>
				   		<input type="text" name="fname" value="{{user['fname']}}" readonly required>
				  		<label>Eftirnafn:</label>
				  		<input type="text" name="lname" value="{{user['lname']}}" readonly required>
				  		<label>Kennitala:</label>
				  		<input type="text" name="ssn" value="{{user['ssn']}}" readonly required>
				  		<label>Phone:</label>
				  		<input type="Phone" name="phone" value="{{user['phone']}}" pattern="\d{3}(?:[\-\s]?)\d{4}" title="Sláðu inn 7 tölustafi" readonly required>
				  		<label>Mail:</label>
				  		<input type="mail" name="mail" value="{{user['mail']}}" pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$" readonly required >
				  		
				  	% else: 
				  		<label>Notandanafn:</label>
				  		<input type="text" name="user" required>
				  		<label>Fornafn:</label>
				  		<input type="text" name="fname" required>
				  		<label>Eftirnafn:</label>
				  		<input type="text" name="lname" required>
				  		<label>Kennitala:</label>
				  		<input type="text" name="ssn" required>
				  		<label>Phone:</label>
				  		<input type="Phone" name="phone" pattern="\d{3}(?:[\-\s]?)\d{4}" title="Sláðu inn 7 tölustafi" required>
				  		<label>Mail:</label>
				  		<input type="mail" name="mail" pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$" required >
				  		
				  	% end
				  	

			  		
			  	</div>
			  	<input id="date" placeholder="checkin: " type="date" value="{{herbergi_uppl['checkin']}}" name="checkin" required readonly >
			  	<input placeholder="checkout: " id="date" type="date" name="checkout" value="{{herbergi_uppl['checkout']}}" required readonly> 
			</div>
			<input type="submit" name="Klára pöntun" value="Klára pöntun">
		</form>
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
  
</body>
</html>
<script>
var login = document.getElementById('id01');

window.onclick = function(event) {
    if (event.target == login) {
        login.style.display = "none";
    }
}
var login = document.getElementById('id02');

window.onclick = function(event) {
    if (event.target == login) {
        login.style.display = "none";
    }
}
</script>

</body>


<script>
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