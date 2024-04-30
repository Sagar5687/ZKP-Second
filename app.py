from flask import Flask, render_template, request, redirect
import hashlib
import os
import time
import jsonify
app = Flask(__name__)
user_session = {'logged_in': False}

def verify_password(password, stored_password_hash):
    # Implement password verification logic here
    # Return True if the provided password matches the stored hash, False otherwise
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    x = int(password_hash, 16)
    return x == int(stored_password_hash)

def get_stored_password_hash(user):
    user_file = f"client/{user}pass.txt"
    try:
        with open(user_file, "r") as f:
            lines = f.readlines()
            stored_password_hash = lines[0].strip()
            return stored_password_hash
    except FileNotFoundError:
        pass
    return None

with open('server/servervalues/g64.txt', 'r') as f:
    g = int(f.read().strip())

with open('server/servervalues/n64.txt', 'r') as f:
    n = int(f.read().strip())

with open('server/servervalues/y.txt', 'r') as f:
    y = int(f.read().strip())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        loc = 'server/userdata/'
        file = loc + user + '.txt'
        secret = 'client/' + user + 'pass.txt'
        
        rkey = hashlib.sha256(password.encode())
        rkey_dig = rkey.hexdigest()
        x = int(rkey_dig, 16)

        A = pow(g, x, n)

        secret_dir = os.path.dirname(secret)
        if not os.path.exists(secret_dir):
            os.makedirs(secret_dir)

        with open(file, "w") as f:
            f.write(str(A))

        with open(secret, "w") as xvalue:
            xvalue.write(str(x))

        return redirect('/')
    return render_template('register.html')

@app.route('/authorize', methods=['GET', 'POST'])
def authorize():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        stored_password_hash = get_stored_password_hash(username)
        
        if stored_password_hash and verify_password(password, stored_password_hash):
            # ZKP logic
            g = int(open('server/servervalues/g64.txt').read().rstrip('\n'))
            n = int(open('server/servervalues/n64.txt').read().rstrip('\n'))
            y = int(open('server/servervalues/y.txt').read().rstrip('\n'))

            user_file = f"server/userdata/{username}.txt"
            A = int(open(user_file).read().rstrip('\n'))

            secret = f"client/{username}pass.txt"
            x = int(open(secret).read().rstrip('\n'))

            q = (x + y) % (n - 1)
            val1 = pow(g, q, n)
            c = pow(g, y, n)

            with open(f"server/userdata/{username}value.txt", "w") as e:
                e.write(str(val1))

            with open(f"server/userdata/{username}challenge.txt", "w") as f:
                f.write(str(c))

            A = int(open(f"server/userdata/{username}value.txt").read().strip())
            c = int(open(f"server/userdata/{username}challenge.txt").read().strip())
            b = int(open(user_file).read().strip())

            d = c * b
            k2 = d % n

            if A == k2:
                # Authorization successful
                with open('server/sensitive-data/data.txt', 'r') as f:
                    data = f.read().strip()
                user_session['logged_in'] = True
                return redirect('success')
            else:
                # Authorization failed
                return render_template('failure.html', message="Authorization failed. ZKP verification failed.")
        else:
            return render_template('failure.html', message="Authorization failed. ZKP verification failed.")

    # If request method is GET, render the authorize.html template
    return render_template('authorize.html', message=None)

@app.route('/success')
def success():
    if user_session.get('logged_in'):
        return render_template('success.html')
    else:
        return redirect('authorize')

@app.route('/logout')
def logout():
    user_session['logged_in'] = False
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)
