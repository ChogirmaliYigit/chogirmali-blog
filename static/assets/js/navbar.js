document.addEventListener("DOMContentLoaded", function () {
    if (window.location.pathname === '/') {
        const defaultLanguage = localStorage.getItem("languageCode")
        if (defaultLanguage) {
            window.location.href = `/${defaultLanguage}/`;
        } else {
            // Redirect to the default language URL
            window.location.href = "/{{ current_language }}/";
            localStorage.setItem("languageCode", "{{ current_language }}");
        }
    }

    // Check if the user has a theme preference saved in local storage
    const isDarkMode = localStorage.getItem("darkMode") === "true";

    // Set the initial theme based on the user's preference
    setTheme(isDarkMode);

    // Set the initial state of the switch
    const themeSwitch = document.getElementById("themeSwitch");
    themeSwitch.checked = isDarkMode;

    // Add an event listener to the theme switch
    themeSwitch.addEventListener("change", function () {
        // Toggle the theme on switch change
        const isDarkMode = this.checked;
        setTheme(isDarkMode);
        // Save the theme preference in local storage
        localStorage.setItem("darkMode", JSON.stringify(isDarkMode));
    });

    // Add an event listener to the search input for the "Enter" key press
    const searchInput = document.getElementById("searchQuery");
    searchInput.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            event.preventDefault();
            document.getElementById("searchForm").submit();
        }
    });

    function setTheme(isDarkMode) {
        const themeStyleLink = document.getElementById("theme-style");
        const markdownStyleLink = document.getElementById("markdown-theme");

        // Update the link to the appropriate CSS file
        themeStyleLink.href = isDarkMode ? "{% static 'assets/css/dark-mode.css' %}" : "{% static 'assets/css/light-mode.css' %}";
        markdownStyleLink.href = isDarkMode ? "{% static 'assets/css/markdown-dark.css' %}" : "{% static 'assets/css/markdown-light.css' %}";

        isDarkMode
            ? document.body.classList.add("dark-content")
            : document.body.classList.remove("dark-content");
    }

    const languageDropdownContainer = document.getElementById("languageDropdownContainer");

    // Add an event listener to the language dropdown items
    languageDropdownContainer.addEventListener("click", function (event) {
        const target = event.target;

        // Check if the clicked element is a dropdown item
        if (target.classList.contains("dropdown-item")) {
            event.preventDefault();

            // Get the language code from the data-language attribute
            const languageCode = target.getAttribute("data-language");

            // Update the URL with the new language code
            const currentUrl = window.location.href;
            const updatedUrl = updateUrlLanguage(currentUrl, languageCode);

            // Redirect to the updated URL
            window.location.href = updatedUrl;
            localStorage.setItem("languageCode", languageCode);
        }
    });

    function updateUrlLanguage(url, newLanguage) {
        // Extract the current language code from the URL
        const languageMatch = url.match(/\/(en|uz)\//i);

        if (languageMatch && languageMatch[1]) {
            const currentLanguage = languageMatch[1];

            // Replace the current language code with the new language code
            const updatedUrl = url.replace(`/${currentLanguage}/`, `/${newLanguage}/`);
            return updatedUrl;
        }

        return url;
    }
});
