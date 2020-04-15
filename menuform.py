from flask import url_for, render_template, redirect, request

from wtforms import Form, StringField, SubmitField, FieldList, FormField, BooleanField
from logger import log
from menubot import MenuBot

tmp = MenuBot()

class MenuItemForm(Form):
    query = StringField('query')
    reply = StringField('reply')
    active = BooleanField('active')


class MenuForm(Form):
    items = FieldList(FormField(MenuItemForm))

    submit = SubmitField('Submit')

    def http(self):
        log( "http "+request.method )
        form = MenuForm(request.form)
        if request.method == 'POST' and form.validate():
            items = []
            for index in range(0, len(request.form) ):
                try:
                    si = str(index)
                    q = 'items-' + si +'-query'
                    r = 'items-' + si +'-reply'
                    a = 'items-' + si +'-active'
                    if q not in request.form:
                        continue
                    qv = request.form[q]
                    if len(qv) < 1:
                        continue
                    rv = request.form[r]
                    if a not in request.form:
                        av = False
                    else:
                        av = request.form[a] == 'y'
                    d = { "query": qv, "reply": rv, "active": av }
                    items.append(d)
                except Exception as e:
                    log( e )

            tmp.menu = items
            tmp.saveMenu()
            return redirect(url_for('success'))

        tmp.loadMenu()
        for row in tmp.menu:
            item_form = MenuItemForm()
            item_form.query = row['query']
            item_form.reply = row['reply']
            item_form.active = row['active']

            form.items.append_entry(item_form)
        # blank field for add
        item_form = MenuItemForm()
        item_form.query = ""
        item_form.reply = ""
        item_form.active = False
        form.items.append_entry(item_form)

        r = render_template('menu.html', form=form)
        return r
