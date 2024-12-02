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