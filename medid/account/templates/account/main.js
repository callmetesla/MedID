var onlyentry = {
    username: "USER",
    password: "1234"
}

var docentry = {
    username: "DOC",
    password: "1234"
}

var pharentry = {
    username: "PHAR",
    password: "1234"
}

var user_data1 = document.getElementById("tagnumber");
var test = document.getElementById('test');
var doclogin = document.getElementById('doclogin');
var pharlogin = document.getElementById('pharlogin');
var doc_data1 = document.getElementById('username');
var doc_data2 = document.getElementById('password');
var phar_data1 = document.getElementById('username_p');
var phar_data2 = document.getElementById('password_p');
var count=0;
function user()
{
    if(user_data1.value != "")
    {
      document.getElementById("otp").innerHTML = "LOGIN";
      count++;
       if( count >= 2)
       {
         var username = document.getElementById("tagnumber");
         var password = document.getElementById("otpnumber");
          if (username.value == onlyentry.username && password.value == onlyentry.password)
           {
         //  console.log(test);
           test.href = "profile_user.html";
           }
       }
    }
}

function doc()
{
   if(doc_data1.value != "" && doc_data2.value !="")
   {
     if (doc_data1.value == docentry.username && doc_data2.value == docentry.password)
     {
       console.log(doclogin);
       doclogin.href = "profile_doc.html";
     }
   }
}


function phar()
{
   if(phar_data1.value != "" && phar_data2.value !="")
   {
     if (phar_data1.value == pharentry.username && phar_data2.value == pharentry.password)
     {
       console.log(pharlogin);
       pharlogin.href = "profile_phar.html";
     }
   }
}
