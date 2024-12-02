// Cursor Initialization
const cursor = document.querySelector('.custom-cursor');

let cursorX = 0;
let cursorY = 0;
let targetX = 0;
let targetY = 0;

// Smooth animation loop
function animateCursor() {
    cursorX += (targetX - cursorX) * 0.2; // Smooth transition effect
    cursorY += (targetY - cursorY) * 0.25;

    cursor.style.transform = `translate(${cursorX}px, ${cursorY}px)`;
    requestAnimationFrame(animateCursor);
}

// Track mouse movement
document.addEventListener('mousemove', (e) => {
    targetX = e.clientX;
    targetY = e.clientY;
});

// Add hover effects to interactive elements
const interactiveElements = document.querySelectorAll('button, a, .feature-card');

interactiveElements.forEach((element) => {
    element.addEventListener('mouseenter', () => {
        cursor.style.transform = 'scale(1.6)';  // Larger scale
        cursor.style.backgroundColor = 'rgba(255, 193, 7, 0.9)';
        cursor.style.boxShadow = '0 0 15px rgba(255, 193, 7, 0.6), 0 0 30px rgba(255, 193, 7, 0.4)';
    });

    element.addEventListener('mouseleave', () => {
        cursor.style.transform = 'scale(1)';  // Back to normal size
        cursor.style.backgroundColor = 'rgba(0, 188, 212, 0.7)';
        cursor.style.boxShadow = '0 0 10px rgba(0, 188, 212, 0.4), 0 0 20px rgba(0, 188, 212, 0.2)';
    });
});

//  document.getElementById('hamburger').addEventListener('click', function(e){
//         console.log("clicked inside the ul");
//         document.getElementById('nav-content').style.display = 'block';
//     }, false)


// Start the animation loop
animateCursor();

const hamburger = document.getElementById("hamburger");
const navContent = document.getElementById("nav-content");
const user = document.getElementById("user");
const userContent = document.getElementById("user-content");


hamburger.addEventListener("click", () => {
  const isOpen = navContent.classList.contains("open");
  
  if (isOpen) {
    navContent.classList.remove("open");
    navContent.classList.add("closed");
    user.removeAttribute("disabled");
  } else {
    navContent.classList.remove("closed");
    navContent.classList.add("open");
    user.setAttribute("disabled", "");

  }

  hamburger.classList.toggle("is-active");
});



user.addEventListener("click", () => {
  const isOpen = userContent.classList.contains("open");
  
  if (isOpen) {
    userContent.classList.remove("open");
    userContent.classList.add("closed");
    hamburger.removeAttribute("disabled");
  } else {
    userContent.classList.remove("closed");
    userContent.classList.add("open");
    hamburger.setAttribute("disabled", "");
  }

  user.classList.toggle("is-active");
});
