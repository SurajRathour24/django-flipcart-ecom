const el = document.getElementById('showsubmenu');

const hiddenDiv = document.getElementById('hiddensubmenu');

// ✅ Show hidden DIV on hover
el.addEventListener('mouseover', function handleMouseOver() {
    hiddensubmenu.style.display = 'block';

  // 👇️ if you used visibility property to hide div
  // hiddenDiv.style.visibility = 'visible';
});

// ✅ (optionally) Hide DIV on mouse out
el.addEventListener('mouseout', function handleMouseOut() {
    hiddensubmenu.style.display = 'none';

  // 👇️ if you used visibility property to hide div
  // hiddenDiv.style.visibility = 'hidden';
});

function change_image(image){
  var container = document.getElementById("main-image");

 container.src = image.src;
}
document.addEventListener("DOMContentLoaded", function(event) {

});