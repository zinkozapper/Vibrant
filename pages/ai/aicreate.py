import os

def create_html_files(start_index=2, end_index=4, css_filename="style.css"):
    """
    Creates a series of HTML files (e.g., ai2.html, ai3.html, ...)
    that all link to a common stylesheet and have the same content.
    """

    # --- 1. Define the reusable HTML content ---
    # The content includes a link to the shared CSS file.
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Page {index}</title>
    <link rel="stylesheet" href="{css_file}">
</head>
<body>
    <header>
        <h1>Welcome to AI Page {index}</h1>
    </header>
    <main>
        <p>This is the standard, shared content for all AI pages.</p>
        <p>It's a demonstration of how a single Python script can generate
           multiple static pages quickly using a common template.</p>
        <div class="content-box">
            <h2>Shared Content Box</h2>
            <p>Every page has this box, styled by <code>{css_file}</code>.</p>
        </div>
    </main>
    <footer>
        <p>&copy; 2025 Generated Pages</p>
    </footer>
</body>
</html>
"""

    # --- 2. Generate the HTML files ---
    print(f"Starting to generate HTML files from ai{start_index}.html to ai{end_index}.html...")

    for i in range(start_index, end_index + 1):
        filename = f"ai{i}.html"

        # Format the template with the current index and CSS filename
        content = html_template.format(index=i, css_file=css_filename)

        try:
            with open(filename, 'w') as f:
                f.write(content)
            print(f"  - Successfully created {filename}")
        except IOError as e:
            print(f"  - Error writing file {filename}: {e}")

    print("\nHTML file generation complete.")

# --- 3. Create the placeholder CSS file ---

# --- 4. Main execution block ---
if __name__ == "__main__":
    css_name = "ai.css"
    create_html_files(start_index=2, end_index=10, css_filename=css_name)
