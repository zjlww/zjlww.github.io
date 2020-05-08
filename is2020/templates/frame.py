
def header(title):
    header = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
        <title>{title}</title>

        <!-- Bootstrap -->
        <link href="/statics/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>

    <div class="container">
    """
    return header

def footer():
    footer = """
    </div>
    <script src="/statics/jquery/jquery-1.12.4.min.js"></script>
    <script src="/statics/bootstrap/js/bootstrap.min.js"></script>
    </body>
    </html>
    """
    return footer
