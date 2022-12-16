from flask import Flask, render_template, jsonify, request
import pyodbc
app = Flask(__name__, template_folder="html")
#Connect to Database
def connection():
    s = 'AN0N1MYS-PK' #Your server name
    d = 'development'
    cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+s+';DATABASE='+d+';Trusted_connection=yes'
    conn = pyodbc.connect(cstr)
    return conn

#Animals
def getAnimals():
    animals = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dbo.animal")
    for row in cursor.fetchall():
        animals.append({"id_animal": row[0], "name": row[1], "age": row[2], "sex": row[3], "breed_id_breed": row[4], "client_id_client": row[5]})
    conn.close()
    return animals

def getAnimal(id_animal):
    assert isinstance(id_animal, int)

    animals = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM dbo.animal where id_animal = {id_animal}")
    for row in cursor.fetchall():
        animals.append({"id_animal": row[0], "name": row[1], "age": row[2], "sex": row[3], "breed_id_breed": row[4],
                        "client_id_client": row[5]})
    conn.close()
    return animals[0]

def updateAnimal(id_animal, name, age, sex, breed_id_breed,client_id_client):
    assert isinstance(id_animal, int)
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(f"UPDATE dbo.animal SET name='{name}',age='{age}',sex='{sex}',breed_id_breed='{breed_id_breed}', client_id_client='{client_id_client}'  WHERE id_animal = {id_animal}")
    conn.commit()
    conn.close()
    return True
def insertAnimal(name, age, sex, breed_id_breed,client_id_client):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO dbo.animal (name, age, sex, breed_id_breed,client_id_client) OUTPUT Inserted.id_animal VALUES" +
        f"('{name}','{age}','{sex}','{breed_id_breed}','{client_id_client}')")
    id_animal = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return id_animal
def deleteAnimal(id_animal):
    assert isinstance(id_animal, int)
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM dbo.animal WHERE id_animal={id_animal};")
    conn.commit()
    conn.close()
    return True
@app.route("/admin/animals")
def animals_view():
    animals = getAnimals()
    return render_template("animal_admin.html", animals= animals)

@app.route("/animals")
def animals_list():

    animals = getAnimals()
    return render_template("animal_list.html", animals= animals)
@app.route("/get_animals", methods=["GET"])
def animals():
    animals = getAnimals()
    return jsonify(animals)


@app.route("/admin/animal/<int:id_animal>", methods=["POST", "GET", "DELETE", "UPDATE"])
def animal(id_animal):
    if request.method == 'GET':
        return jsonify(getAnimal(id_animal))
    elif request.method == 'POST':
        form = request.get_json()
        id_animal = insertAnimal(form["name"], form["age"], form["sex"], form["breed_id_breed"], form["client_id_client"])
        return jsonify({"id_animal":id_animal})
    elif request.method == 'UPDATE':
        form = request.get_json()
        id_animal = updateAnimal(id_animal, form["name"], form["age"], form["sex"], form["breed_id_breed"], form["client_id_client"])
        return jsonify({"id_animal":id_animal})
    else:
        return jsonify({"status": deleteAnimal(id_animal)})


#Client
def getClients():
    clients = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dbo.client")
    for row in cursor.fetchall():
        clients.append({"id_client": row[0], "fio": row[1], "phone": row[2], "email": row[3]})
    conn.close()
    return clients

def getClient(id_client):
    assert isinstance(id_client, int)

    clients = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM dbo.client where id_client = {id_client}")
    for row in cursor.fetchall():
        clients.append({"id_client": row[0], "fio": row[1], "phone": row[2], "email": row[3]})
    conn.close()
    return clients[0]

def updateClient(id_client, fio, phone, email):
    assert isinstance(id_client, int)
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(f"UPDATE dbo.client SET fio='{fio}',phone='{phone}',email='{email}' WHERE id_client = {id_client}")
    conn.commit()
    conn.close()
    return True
def insertClient(fio, phone, email):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO dbo.client (fio, phone, email) OUTPUT Inserted.id_client VALUES " +
        f"('{fio}','{phone}','{email}')")
    id_client = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return id_client
def deleteClient(id_client):
    assert isinstance(id_client, int)
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM dbo.client WHERE id_client={id_client};")
    conn.commit()
    conn.close()
    return True
@app.route("/admin/clients")
def clients_view():
    clients = getClients()
    return render_template("client_admin.html", clients= clients)

@app.route("/clients")
def clients_list():

    clients = getClients()
    return render_template("client_list.html", clients = clients)

@app.route("/get_clients", methods=["GET"])
def clients():
    clients = getClients()
    return jsonify(clients)


@app.route("/admin/client/<int:id_client>", methods=["POST", "GET", "DELETE", "UPDATE"])
def client(id_client):
    if request.method == 'GET':
        return jsonify(getClient(id_client))
    elif request.method == 'POST':
        form = request.get_json()
        id_client = insertClient(form["fio"], form["phone"], form["email"])
        return jsonify({"id_client":id_client})
    elif request.method == 'UPDATE':
        form = request.get_json()
        id_client = updateClient(id_client, form["fio"], form["phone"], form["email"])
        return jsonify({"id_client":id_client})
    else:
        return jsonify({"status": deleteClient(id_client)})

#Worker
def getWorkers():
    workers = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dbo.worker")
    for row in cursor.fetchall():
        workers.append({"id_worker": row[0], "fio": row[1],  "email": row[2],"phone": row[3],"sex": row[4],"post_id_post": row[5]})
    conn.close()
    return workers

def getWorker(id_worker):
    assert isinstance(id_worker, int)
    workers = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM dbo.worker where id_worker = {id_worker}")
    for row in cursor.fetchall():
        workers.append({"id_worker": row[0], "fio": row[1], "email": row[2], "phone": row[3], "sex": row[4], "post_idd_post": row[5]})
    conn.close()
    return workers[0]

def updateWorker(id_worker, fio,email, phone, sex, post_id_post):
    assert isinstance(id_worker, int)
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(f"UPDATE dbo.worker SET fio='{fio}',email='{email}',phone='{phone}',sex='{sex}',post_id_post='{post_id_post}' WHERE id_worker = {id_worker}")
    conn.commit()
    conn.close()
    return True
def insertWorker(fio, email,phone,sex,post_id_post):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO dbo.worker (fio,  email, phone, sex, post_id_post) OUTPUT Inserted.id_worker VALUES " +
        f"('{fio}','{email}','{phone}','{sex}','{post_id_post}')")
    id_worker = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return id_worker
def deleteWorker(id_worker):
    assert isinstance(id_worker, int)
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM dbo.worker WHERE id_worker={id_worker};")
    conn.commit()
    conn.close()
    return True
@app.route("/admin/workers")
def workers_view():
    workers = getWorkers()
    return render_template("worker_admin.html", workers= workers)

@app.route("/workers")
def workers_list():

    workers = getWorkers()
    return render_template("worker_list.html", workers = workers)

@app.route("/get_workers", methods=["GET"])
def workers():
    workers = getWorkers()
    return jsonify(workers)


@app.route("/admin/worker/<int:id_worker>", methods=["POST", "GET", "DELETE", "UPDATE"])
def worker(id_worker):
    if request.method == 'GET':
        return jsonify(getWorker(id_worker))
    elif request.method == 'POST':
        form = request.get_json()
        id_worker = insertWorker(form["fio"], form["email"], form["phone"], form["sex"], form["post_id_post"] )
        return jsonify({"id_worker":id_worker})
    elif request.method == 'UPDATE':
        form = request.get_json()
        id_worker = updateWorker(id_worker, form["fio"], form["email"], form["phone"], form["sex"], form["post_id_post"])
        return jsonify({"id_worker":id_worker})
    else:
        return jsonify({"status": deleteWorker(id_worker)})


#Post
def getPosts():
    posts = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dbo.post")
    for row in cursor.fetchall():
        posts.append({"id_post": row[0], "title": row[1]})
    conn.close()
    return posts

def getPost(id_post):
    assert isinstance(id_post, int)
    posts = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM dbo.post where id_post = {id_post}")
    for row in cursor.fetchall():
        posts.append({"id_post": row[0], "title": row[1]})
    conn.close()
    return posts[0]

def updatePost(id_post, title):
    assert isinstance(id_post, int)
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(f"UPDATE dbo.post SET title='{title}' WHERE id_post = {id_post}")
    conn.commit()
    conn.close()
    return True
def insertPost(title):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO dbo.post (title) OUTPUT Inserted.id_post VALUES " +
        f"('{title}')")
    id_post = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return id_post
def deletePost(id_post):
    assert isinstance(id_post, int)
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM dbo.post WHERE id_post={id_post};")
    conn.commit()
    conn.close()
    return True
@app.route("/admin/posts")
def posts_view():
    posts = getPosts()
    return render_template("post_admin.html", posts= posts)

@app.route("/posts")
def posts_list():
    posts = getPosts()
    return render_template("post_list.html", posts = posts)

@app.route("/get_posts", methods=["GET"])
def posts():
    posts = getPosts()
    return jsonify(posts)


@app.route("/admin/post/<int:id_post>", methods=["POST", "GET", "DELETE", "UPDATE"])
def post(id_post):
    if request.method == 'GET':
        return jsonify(getPost(id_post))
    elif request.method == 'POST':
        form = request.get_json()
        id_post = insertPost(form["title"])
        return jsonify({"id_post":id_post})
    elif request.method == 'UPDATE':
        form = request.get_json()
        id_post = updatePost(id_post, form["title"])
        return jsonify({"id_post":id_post})
    else:
        return jsonify({"status": deletePost(id_post)})

#Breed
def getBreeds():
    breeds = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dbo.breed")
    for row in cursor.fetchall():
        posts.append({"id_breed": row[0], "title": row[1]})
    conn.close()
    return breeds

def getBreed(id_breed):
    assert isinstance(id_breed, int)
    breeds = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM dbo.breed where id_breed = {id_breed}")
    for row in cursor.fetchall():
        posts.append({"id_breed": row[0], "title": row[1]})
    conn.close()
    return breeds[0]

def updateBreed(id_breed, title):
    assert isinstance(id_breed, int)
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(f"UPDATE dbo.breed SET title='{title}' WHERE id_breed = {id_breed}")
    conn.commit()
    conn.close()
    return True
def insertBreed(title):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO dbo.breed (title) OUTPUT Inserted.id_breed VALUES " +
        f"('{title}')")
    id_breed = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return id_breed
def deleteBreed(id_breed):
    assert isinstance(id_breed, int)
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM dbo.breed WHERE id_breed={id_breed};")
    conn.commit()
    conn.close()
    return True
@app.route("/admin/breeds")
def breeds_view():
    breeds = getBreeds()
    return render_template("breed_admin.html", breeds= breeds)

@app.route("/breeds")
def breeds_list():
    breeds = getBreeds()
    return render_template("breed_list.html", breeds = breeds)

@app.route("/get_breeds", methods=["GET"])
def breeds():
    breeds = getBreeds()
    return jsonify(breeds)


@app.route("/admin/breed/<int:id_breed>", methods=["POST", "GET", "DELETE", "UPDATE"])
def breed(id_breed):
    if request.method == 'GET':
        return jsonify(getBreed(id_breed))
    elif request.method == 'POST':
        form = request.get_json()
        id_breed = insertBreed(form["title"])
        return jsonify({"id_breed":id_breed})
    elif request.method == 'UPDATE':
        form = request.get_json()
        id_breed = updateBreed(id_breed, form["title"])
        return jsonify({"id_breed":id_breed})
    else:
        return jsonify({"status": deleteBreed(id_breed)})



#All
@app.route("/")
def main():
    return render_template("index.html")


if(__name__ == "__main__"):
    app.run()
