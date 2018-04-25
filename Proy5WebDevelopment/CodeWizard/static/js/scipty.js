$(document).ready(function(){
  console.log("Loaded");
  $.material.init();

  $(document).on("submit", "#register-form", function(e){
    e.preventDefault();
    console.log("Form submitted");
    var form = $("#register-form" ).serialize();
    $.ajax({
      url: '/postregistration',
      type: 'POST',
      data: form,
      success: function(response){
        console.log(response);
      }
    });
  });

  $(document).on("submit", "#login-form", function(e){
    e.preventDefault();
    var form = $("#login-form").serialize();
    $.ajax({
      url: '/check-login',
      type: 'POST',
      data: form,
      success: function(res){
        if (res == "error"){
          console.log("No login ");
          alert("Could not log in");
        }else{
          console.log("Logged in as ",res);
          window.location.href = "/";
        }
      }
    })
  });
});
