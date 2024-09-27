from flask import Flask, url_forimport dominatefrom dominate.tags import *app = Flask(__name__)@app.route('/')def home():    doc = dominate.document(title='Home Page')    with doc.head:        link(rel='stylesheet', href='https://fonts.googleapis.com/css?family=Roboto')    # Generate the correct path for the static logo without the leading slash    logo_url = 'static/logo.png'  # Change this line to remove the leading slash    with doc:        doc.add(render_navbar())        with body(style="background-color: rgb(229, 204, 255);"):            with div(style="text-align: center; margin-top: 50px;"):                h1('Welcome to Na Laochra Aeracha Home Page')                p('Cork LGBTQ+ Inclusive GAA (football) Club')                img(src=logo_url, width="400")  # Use the modified URL    return str(doc)        def render_navbar():    nav_bar = nav()    ul_list = ul(style="list-style-type: none; margin: 0; padding: 0; overflow: hidden; background-color: #138;")        # Home Link    ul_list += li(a('Home', href='index.html', style="display: block; color: white; text-align: center; padding: 14px 16px; text-decoration: none;"),                   style="float: left;")        # Galary Link    ul_list += li(a('Gallery', href='gallery.html', style="display: block; color: white; text-align: center; padding: 14px 16px; text-decoration: none;"),                   style="float: left;")    # News Link    ul_list += li(a('News', href='news.html', style="display: block; color: white; text-align: center; padding: 14px 16px; text-decoration: none;"),                   style="float: left;")            # About Link    ul_list += li(a('About', href='about.html', style="display: block; color: white; text-align: center; padding: 14px 16px; text-decoration: none;"),                   style="float: left;")        # Contact Link    ul_list += li(a('Contact', href='contact.html', style="display: block; color: white; text-align: center; padding: 14px 16px; text-decoration: none;"),                   style="float: left;")        nav_bar.add(ul_list)    return nav_bar        @app.route('/about')def about():    doc = dominate.document(title='About')    with doc.head:        link(rel='stylesheet', href='https://fonts.googleapis.com/css?family=Roboto')    with doc:        doc.add(render_navbar())        with body(style="background-color: rgb(229, 204, 255);"):            with div(style="text-align: center; margin-top: 50px;"):                h1('About')                p('The Na Laochra Aeracha is the first LGBTQ+ Inclusve Gaelic Footabll Club. Training is every Wednesday 18:30 to 19:30 and Sundays 10:30 to 11:30.')            with div(style="text-align: center; margin-top: 50px;"):                h1('Team Members')                                              return str(doc)        @app.route('/news')def news():    doc = dominate.document(title='News')    with doc.head:        link(rel='stylesheet', href='https://fonts.googleapis.com/css?family=Roboto')    with doc:        doc.add(render_navbar())        with body(style="background-color: rgb(229, 204, 255);"):            with div(style="text-align: center; margin-top: 50px;"):                h1('News')                h2('Be Active- September 2024')                                p('SportFest LGBTQ+ GAA Session Sat, 28th Sep 2024 @6pm Tramore Valley Park, Cork.')                a(img(src="static/News/News1.jpg", width="250"), href="static/News/News1.jpg")                return str(doc)        @app.route('/contact')def contact():    doc = dominate.document(title='Contact')    with doc.head:        link(rel='stylesheet', href='https://fonts.googleapis.com/css?family=Roboto')    with doc:        doc.add(render_navbar())        with body(style="background-color: rgb(229, 204, 255);"):            with div(style="text-align: center; margin-top: 50px;"):                h1('Contact Us')                p(' You can contact Na Laochra Aeracha through our Instagram page: @na_laochra_aeracha')                                               return str(doc)@app.route('/gallery')def gallery():    doc = dominate.document(title='Gallery')    with doc.head:        link(rel='stylesheet', href='https://fonts.googleapis.com/css?family=Roboto')    with doc:        doc.add(render_navbar())        with body(style="background-color: rgb(229, 204, 255);"):            h1('Gallery', style="text-align: center;")            p('Images from the training sessions on Wednesdays and Sundays!',  style="text-align: center;")            with table(border="1", style="width:100%", cellpadding="10"):                with tr():  # First row                    with td():  # First cell of the first row                        # Add a clickable image                        p('25th of Semptember 2024 at Glen River Park')                        a(img(src="static/IMG-20240925.jpg", width="250"), href="static/IMG-20240925.jpg")                                        with td():  # Second cell of the first row                        p('22nd of Semptember 2024 at Tramore Valley Park')                        a(img(src="static/IMG-20240922.jpg", width="250"), href="static/IMG-20240922.jpg")                    with td():  # Second cell of the first row                        p('18th of Semptember 2024 at Glen River Park')                        a(img(src="static/IMG-20240918.jpg", width="250"), href="static/IMG-20240918.jpg")                                    with tr():  # Second row                    with td():  # Second cell of the first row                        p('11th of Semptember 2024 at Glen River Park')                        a(img(src="static/IMG-20240911.jpg", width="250"), href="static/IMG-20240911.jpg")                    with td():  # Second cell of the first row                        p('4th of Semptember 2024 at Glen River Park')                        a(img(src="static/IMG-20240904.jpg", width="250"), href="static/IMG-20240904.jpg")                                            with td():  # Second cell of the first row                        p('3rd of August 2024 at Vibe')                        a(img(src="static/IMG-20240901.jpg", width="250"), href="static/IMG-20240901.jpg")    return str(doc)    def save_static_html(filename='index.html'):    # Generate HTML content from the home route    with app.test_request_context('/'):        html_content = home()        # Save the HTML content to a file        with open(filename, 'w') as f:            f.write(html_content)def save_static_html_about(filename='about.html'):    # Generate HTML content from the home route    with app.test_request_context('/about'):        html_content = about()        # Save the HTML content to a file        with open(filename, 'w') as f:            f.write(html_content)def save_static_html_gallery(filename='gallery.html'):    # Generate HTML content from the home route    with app.test_request_context('/gallery'):        html_content = gallery()        # Save the HTML content to a file        with open(filename, 'w') as f:            f.write(html_content)            def save_static_html_contact(filename='contact.html'):    # Generate HTML content from the home route    with app.test_request_context('/contact'):        html_content = contact()        # Save the HTML content to a file        with open(filename, 'w') as f:            f.write(html_content)def save_static_html_news(filename='news.html'):    # Generate HTML content from the home route    with app.test_request_context('/news'):        html_content = news()        # Save the HTML content to a file        with open(filename, 'w') as f:            f.write(html_content)if __name__ == '__main__':    save_static_html()  # Generate and save the HTML file    save_static_html_about()    save_static_html_gallery()    save_static_html_contact()    save_static_html_news()    app.run(debug=True)  # Start the Flask app