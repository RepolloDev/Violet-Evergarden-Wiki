const gallery = document.getElementById("characters-gallery");
let current = 0;

function showImage() {
  gallery.children[current].style.opacity = 0;
  current = (current + 1) % gallery.children.length;
  gallery.children[current].style.opacity = 1;
}

setInterval(showImage, 3000);
