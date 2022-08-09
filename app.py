from flask import redirect, render_template, request, flash
from models import BLOG, db, app, SQLAlchemy


# view_all_post
@app.route("/")
def home():
    user = BLOG.query.limit(100).all()
    return render_template("content.html", users=user)


# update the post
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    update = BLOG.query.get_or_404(id)

    if request.method == "POST":
        update.company_name = request.form["company_name"]
        update.email = request.form["email"]
        update.phone_number = request.form["phone_number"]
        update.address = request.form["address"]

        db.session.add(update)
        db.session.commit()

        return redirect("/")
    return render_template("edit.html", update=update)


# delete the post


@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    delete_post = BLOG.query.get_or_404(id)
    db.session.delete(delete_post)
    db.session.commit()
    flash("Post is deleted")
    return redirect("/")


# add_post
@app.route("/link", methods=["GET", "POST"])
def link():
    if request.method == "POST":

        company_name = request.form["company_name"]
        email = request.form["email"]
        phone_number = request.form["phone_number"]
        address = request.form["address"]

        data = BLOG(company_name, email, phone_number, address)
        db.session.add(data)
        db.session.commit()
        flash("Data is added")

        return redirect("/")

    return render_template("post.html")


if __name__ == "__main__":
    app.run(debug=True)
