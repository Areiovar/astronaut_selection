from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/astronaut_selection')
def bootstrap():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for ('static', filename='css/style.css')}" />
                                <title>Пример формы</title>
                              </head>
                              <body>
                                <div class="center-both">
                                  <h>Анкета претендента</h></div>
                                  <div class="asd"><h>на участие в миссии</h></div>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="text" class="form-control" id="surname" aria-describedby="emailHelp" placeholder="Введите фамилию" name="surname">
                                        <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email" style="margin-top: 15px;">
                                        <div class="form-group">
                                            <label for="classSelect">Какое у вас образование?</label>
                                            <select class="form-control" id="classSelect" name="class">
                                              <option>Дошкольное</option>
                                              <option>Начальное общее — 1—4 классы</option>
                                              <option>Основное общее — 5—9 классы</option>
                                              <option>Среднее общее — 10—11 классы</option>
                                              <option>Среднее профессиональное</option>
                                              <option>Высшее I степени — бакалавриат</option>
                                              <option>Высшее II степени — специалитет, магистратура</option>
                                              <option>Высшее III степени — подготовка кадров высшей квалификации</option>
                                            </select>
                                         </div>
                                        <div class="form-group" style="margin-top: 15px;">
                                            <label>Какие у вас есть профессии?</label><br>
                                            <div class="form-check">
                                                <input class="form-check-input" type="radio" name="profession" id="engineer-researcher" value="engineer-researcher">
                                                <label class="form-check-label" for="engineer-researcher">Инженер-исследователь</label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="radio" name="profession" id="pilot" value="pilot">
                                                <label class="form-check-label" for="pilot">Пилот</label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="radio" name="profession" id="builder" value="builder">
                                                <label class="form-check-label" for="builder">Строитель</label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="radio" name="profession" id="exobiologist" value="exobiologist">
                                                <label class="form-check-label" for="exobiologist">Экзобиолог</label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="radio" name="profession" id="doctor" value="doctor">
                                                <label class="form-check-label" for="doctor">Врач</label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="radio" name="profession" id="terraform-engineer" value="terraform-engineer">
                                                <label class="form-check-label" for="terraform-engineer">Инженер по терраформированию</label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="radio" name="profession" id="climatologist" value="climatologist">
                                                <label class="form-check-label" for="climatologist">Климатолог</label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="radio" name="profession" id="radiation-specialist" value="radiation-specialist">
                                                <label class="form-check-label" for="radiation-specialist">Специалист по радиационной защите</label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="radio" name="profession" id="astrogeologist" value="astrogeologist">
                                                <label class="form-check-label" for="astrogeologist">Астрогеолог</label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="radio" name="profession" id="glaciologist" value="glaciologist">
                                                <label class="form-check-label" for="glaciologist">Гляциолог</label>
                                            </div>
                                        <div class="form-group" style="margin-top: 15px;">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check" style="margin-top: 15px;">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female" >
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        </div>
                                        <div class="form-group" style="margin-top: 15px;">
                                            <label for="about">Почему вы хотите принять участие в миссии? </label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>

                                        <div class="form-group" style="margin-top: 15px;">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>

                                        <div class="form-group form-check" style="margin-top: 15px;">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Записаться</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run('127.0.0.1', 8080)
