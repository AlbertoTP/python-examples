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
});
