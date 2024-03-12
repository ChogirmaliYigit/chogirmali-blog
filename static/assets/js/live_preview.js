(function ($) {
    $(document).ready(function () {
        // Function to update the live preview
        function updatePreview(content) {
            // Use markdown-it to render the Markdown content
            var md = window.markdownit();
            var renderedContent = md.render(content);

            // Update the preview container with the rendered content
            $('#id_content').next('.markdown-preview').html(renderedContent);
        }

        // Add a live preview container after the content textarea
        $('#id_content').after('<div class="markdown-preview"></div>');

        // Update the preview on page load
        updatePreview($('#id_content').val());

        // Update the preview when the content changes
        $('#id_content').on('input', function () {
            updatePreview($(this).val());
        });
    });
})(django.jQuery);
