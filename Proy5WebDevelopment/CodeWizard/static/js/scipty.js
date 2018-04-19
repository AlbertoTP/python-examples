$(document).ready(function(){
  console.log("Loaded");
  $.material.init();

  $(document).on("submit","#register-form", function(e){
    e.preventDefault();
    console.log("Form Submited");
  });
});
