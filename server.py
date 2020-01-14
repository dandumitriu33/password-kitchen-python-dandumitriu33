from flask import Flask, render_template, request, redirect
import data_manager


app=Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        background_color = '#1976d2'
        return render_template('home.html',
                               background_color=background_color)
    # elif request.method == 'POST':
    #     # if request.form['hashed-password'] == '':
    #     #     password = request.form['password']
    #     #     hashed = data_manager.hash_password(password)
    #     #     background_color = '#1976d2'
    #     #     return render_template('home.html',
    #     #                            background_color=background_color,
    #     #                            password=password,
    #     #                            hashed=hashed)
    #     if request.form['verify-hashed-password'] != '':
    #         password = request.form['verify-password']
    #         hashed = request.form['verify-hashed-password']
    #         if data_manager.hash_password(password) == hashed:
    #             background_color = '#43a047'
    #             match_message = "It's a match!"
    #             return render_template('home.html',
    #                                    background_color=background_color)
    #         else:
    #             background_color = '#e53935'
    #             match_message = "Doesn't match!"
    #             return render_template('home.html',
    #                                    background_color=background_color)


@app.route('/hash', methods=['GET', 'POST'])
def hash_password():
    if request.method == 'POST':
        password = request.form['password']
        hashed_password = data_manager.hash_password(password)
        background_color = '#1976d2'
        return render_template('home.html',
                               background_color=background_color,
                               password=password,
                               hashed=hashed_password)


@app.route('/verify', methods=['GET', 'POST'])
def verify_password():
    if request.method == 'POST':
        user_password = request.form['verify-password']
        user_hashed_password = request.form['verify-hashed-password']
        if user_hashed_password == data_manager.hash_password(user_password):
            background_color = '#43a047'
            return render_template('home.html',
                                   background_color=background_color,
                                   verify_password=user_password,
                                   verify_hashed_password=user_hashed_password)
        else:
            background_color = '#e53935'
            return render_template('home.html',
                                   background_color=background_color,
                                   verify_password=user_password,
                                   verify_hashed_password=user_hashed_password)


if __name__ == '__main__':
    app.run(debug=True)
