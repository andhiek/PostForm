$(window).scroll(function () {
  scroll = $(window).scrollTop();

  console.log(scroll);

  document.getElementById("myBody").style.marginTop = -100 - 0.5 * scroll + "px";

  if (scroll >= 200) {
    $("#myNav").addClass("bg-dark");
  } else {
    $("#myNav").removeClass("bg-dark");
  }
});
