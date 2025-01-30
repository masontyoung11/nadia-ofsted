document.addEventListener("DOMContentLoaded", function () {
  const home_key = document.querySelector(".home-key");

  function getOS() {
    const userAgent = navigator.userAgent;

    if (userAgent.indexOf("Win") !== -1) {
      return "Windows";
    } else if (userAgent.indexOf("Mac") !== -1) {
      return "MacOS";
    } else if (userAgent.indexOf("Linux") !== -1) {
      return "Linux";
    } else {
      return "Unknown";
    }
  }

  const OS = getOS();

  if (OS === "Windows") {
    home_key.innerHTML = "CTRL";
  } else if (OS === "MacOS") {
    home_key.innerHTML = "⌘";
  } else if (OS === "Linux") {
    home_key.innerHTML = "CTRL";
  } else {
    home_key.innerHTML = "CTRL";
  }

  document.addEventListener("keydown", function (event) {
    if ((OS === "MacOS" && event.metaKey) || (OS !== "MacOS" && event.ctrlKey)) {
      if (event.key === "k") {
        document.body.toggleAttribute('spotlight-open');
      }
    }
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
      if(document.body.hasAttribute('spotlight-open')) {
        document.body.removeAttribute('spotlight-open');
      }
    }
  });

  document.addEventListener("click", function (event) {
    if (event.target.closest('.spotlight')) {
      event.stopPropagation();
    } else if (document.body.hasAttribute('spotlight-open')) {
      if (!event.target.closest('.spotlight-menu')) {
        document.body.removeAttribute('spotlight-open');
      }
    }
  });
});
