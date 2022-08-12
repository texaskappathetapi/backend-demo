# backend-demo

To use this template, click the green **Use as template** button at the top. There are portions removed in the *app/routes.py* file to learn about GET and POST requests.

## Getting started

### Installing dependencies

```shell
pip install Flask Flask-SQLAlchemy Flask-Migrate
```

### Initializing the database

To initialize the database, run

```shell
flask db init
```

once during the duration of development. This will create a folder called *migrations* that holds the migration information.

Run

```shell
flask db migrate
flask db upgrade
```

to migrate and propagate changes to the database if we make changes to the database code structure (found in *app/models.py*).

## Tutorial

1. **Complete the code in *app/routes.py* for the POST request made to the index route when the form is subimtted.**

Note that the HTML file makes a POST request since the form button has a `type="submit"` attribute, where the form contents are passed in the request body (accessed through `flask.request`). Include error handling!
<details>
<summary>Full implementation</summary>

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        short_id = request.form['custom_id']

        if short_id and ShortURLs.query.filter_by(short_id=short_id).first() is not None:
            flash('Please enter different custom id!')
            return redirect(url_for('index'))

        if not url:
            flash('The URL is required!')
            return redirect(url_for('index'))

        if not short_id:
            short_id = generate_short_id(8)

        new_link = ShortURLs(
            original_url=url, short_id=short_id, created_at=datetime.now())
        db.session.add(new_link)
        db.session.commit()
        short_url = request.host_url + short_id

        return render_template('index.html', short_url=short_url)

    return render_template('index.html')
```

</details>


2. **Complete the `redirect_url()` route to redirect to the correct page. Once again, include error handling.**
<details>
<summary>Full implementation</summary>

```python
@app.route('/<short_id>')
def redirect_url(short_id):
    link = ShortURLs.query.filter_by(short_id=short_id).first()
    if link:
        return redirect(link.original_url)
    else:
        flash('Invalid URL')
        return redirect(url_for('index'))
```

</details>
